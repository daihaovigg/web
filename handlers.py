#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio,os

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, AudioList, VideoList, next_id
from config import configs

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

def user2cookie(user, max_age):
    '''
    Generate cookie str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = yield from User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None
    
@get('/')
def index_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    page = Page(num,page_index=page_index)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

@get('/blog/{id}')
def get_blog(id):
    blog = yield from Blog.find(id)
    comments = yield from Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }
import uuid
@get('/register')
def register():
    return {
        '__template__': 'register.html',
        'img_uuid': uuid.uuid1()
    }

@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }

@post('/api/authenticate')
def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = yield from User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r

@get('/manage/')
def manage():
    return 'redirect:/manage/comments'

@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }

@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }

@get('/manage/blogs/edit')
def manage_edit_blog(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id
    }

@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

@get('/api/comments')
def api_comments(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Comment.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = yield from Comment.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

@post('/api/blogs/{id}/comments')
def api_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = yield from Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.name, user_image=user.image, to_who=blog.user_name,content=content.strip())
    yield from comment.save()
    return comment

@post('/api/comments/{id}/delete')
def api_delete_comments(id, request):
    check_admin(request)
    c = yield from Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(id=id)

@get('/api/users')
def api_get_users(request,*, page='1'):
    check_admin(request)
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = yield from User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p, users=users)

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@post('/api/users')
def api_register_user(*, email, name, passwd,img_uuid):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('passwd')
    users = yield from User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIValueError('email', 'Email is already in use.')
    users = yield from User.findAll('name=?', [name])
    if len(users) > 0:
        raise APIValueError('name', 'name is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    img_path="/static/HeadImg/"
    img_path=img_path+img_uuid
    img_path=img_path+".jpg"

    path=os.path.abspath('.')
    path=os.path.join(path,"static")
    path=os.path.join(path,"HeadImg")
    path=os.path.join(path,"%s.jpg" % img_uuid)
    if not os.path.exists(path):
        img_path="/static/img/default.jpg"
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image=img_path)
    yield from user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/api/blogs')
def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)

@get('/api/blogs/{id}')
def api_get_blog(*, id):
    blog = yield from Blog.find(id)
    return blog

@post('/api/blogs')
def api_create_blog(request, *, name, summary, content,id):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip(),id=id)
    yield from blog.save()
    return blog

@post('/api/blogs/{id}')
def api_update_blog(id, request, *, name, summary, content):
    check_admin(request)
    blog = yield from Blog.find(id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    yield from blog.update()
    return blog

@post('/api/blogs/{id}/delete')
def api_delete_blog(request, *, id):
    check_admin(request)
    blog = yield from Blog.find(id)
    yield from blog.remove()
    return dict(id=id)



#######common user manage######
@get('/myapi/comments')
def myapi_comments(request,*, page='1'):
    where_user='to_who='+'\''+request.__user__.name+'\''
    page_index = get_page_index(page)
    num = yield from Comment.findNumber('count(id)',where=where_user)
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = yield from Comment.findAll(where=where_user,orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

@post('/myapi/blogs/{id}/comments')
def myapi_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = yield from Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.name, user_image=user.image, to_who=blog.user_name,content=content.strip())
    yield from comment.save()
    return comment

@post('/myapi/comments/{id}/delete')
def myapi_delete_comments(id, request):
    c = yield from Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(id=id)

@get('/myapi/blogs')
def myapi_blogs(request,*, page='1'):
    where_user='user_name='+'\''+request.__user__.name+'\''
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)',where=where_user)
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from Blog.findAll(where=where_user,orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)

@get('/myapi/blogs/{id}')
def myapi_get_blog(*, id):
    blog = yield from Blog.find(id)
    return blog

@post('/myapi/blogs')
def myapi_create_blog(request, *, name, summary, content,id):
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip(),id=id)
    yield from blog.save()
    return blog


@post('/myapi/blogs/{id}')
def myapi_update_blog(id, request, *, name, summary, content):
    blog = yield from Blog.find(id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    yield from blog.update()
    return blog

@post('/myapi/blogs/{id}/delete')
def myapi_delete_blog(request, *, id):
    #check_admin(request)
    blog = yield from Blog.find(id)
    yield from blog.remove()
    return dict(id=id)


@get('/mymanage/')
def mymanage():
    return 'redirect:/mymanage/blogs'

@get('/mymanage/blogs')
def mymanage_blogs(*, page='1'):
    return {
        '__template__': 'mymanage_blogs.html',
        'page_index': get_page_index(page)
    }

@get('/mymanage/blogs/create')
def mymanage_create_blog():
    return {
        '__template__': 'mymanage_blog_edit.html',
        'id': '',
        'new_id': next_id(),
        'action': '/myapi/blogs'
    }

@get('/mymanage/blogs/edit')
def mymanage_edit_blog(*, id):
    return {
        '__template__': 'mymanage_blog_edit.html',
        'id': id,
        'new_id': '',
        'action': '/myapi/blogs/%s' % id
    }

@get('/mymanage/comments')
def mymanage_comments(*, page='1'):
    return {
        '__template__': 'mymanage_comments.html',
        'page_index': get_page_index(page)
    }

@get('/user/{id}')
def user_blogs(id,*, page='1'):
    where_user='user_name='+'\''+id+'\''
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)',where=where_user)
    page = Page(num,page_index=page_index)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(where=where_user,orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'user_blogs.html',
        'page': page,
        'blogs': blogs,
        'id': id
    }



#####defalut image of HD########



@post('/myapi/uploader/{img_uuid}')
def head_img_upload(request,*,file,img_uuid):
    file.file.seek(0)
    path=os.path.abspath('.')
    path=os.path.join(path,"static")
    path=os.path.join(path,"HeadImg")
    path=os.path.join(path,"%s.jpg" % img_uuid)
    with open(path,"wb") as jpg:
        for i in file.file:
            jpg.write(i)

#######have fun with ball_pool##########
@get('/ball_pool')
def test_show():
    return {
        '__template__': 'ball_pool.html'
    }


#######markdown --help#######
@get('/markdown_help')
def markdown_help():
    return {
        '__template__': 'markdown_help.html'
    }
    
######preview markdown blog######
#@post('/myapi/markdown_translate')
#def markdown_translate():
#    pass

######blog_img_upload######
@post('/myapi/bloguploader')
def blog_img_upload(request,*,file,filename):
    file.file.seek(0)
    suffix=os.path.splitext(file.filename)[1][1:] ##获取后缀名
    if(suffix=='jpg' or suffix=='png' or suffix=='gif'):
        path=os.path.abspath('.')
        path=os.path.join(path,"static")
        path=os.path.join(path,"BlogImg")
        path=os.path.join(path,"%s.%s" % (filename,suffix))
        with open(path,"wb") as img:
            for i in file.file:
                img.write(i)
    elif(suffix=='mp3' or suffix=='ogg'):
        path=os.path.abspath('.')
        path=os.path.join(path,"static")
        path=os.path.join(path,"audio")
        path=os.path.join(path,"%s" % file.filename)
        with open(path,"wb") as aud:
            for i in file.file:
                aud.write(i)
        file_name="/static/audio/"+file.filename
        audiolist = AudioList(src=file_name,name=file.filename)
        yield from audiolist.save()

    elif(suffix=='mp4'):
        path=os.path.abspath('.')
        path=os.path.join(path,"static")
        path=os.path.join(path,"video")
        path=os.path.join(path,"%s" % file.filename)
        with open(path,"wb") as vid:
            for i in file.file:
                vid.write(i)
        file_name="/static/video/"+file.filename
        videolist = VideoList(src=file_name,name=file.filename)
        yield from videolist.save()

    else :
        pass


####redirect audio#####
@get('/blog/static/audio/{audioname}')
def redirect_audio_to_static(audioname):
    return 'redirect: /static/audio/%s' % audioname

####redirect video#####
@get('/blog/static/video/{videoname}')
def redirect_video_to_static(videoname):
    return 'redirect: /static/video/%s' % videoname

#####audioplayer by audiojs#######
@get('/audioplayer')
def audioplayer():
    audios = yield from AudioList.findAll(orderBy='created_at desc')
    return {
        '__template__': 'audio_player.html',
        'audios': audios
    }

#####cideoplayer by dai ######
@get('/videoplayer')
def videoplayer():
    videos = yield from VideoList.findAll(orderBy='created_at desc')
    return {
        '__template__': 'video_player.html',
        'videos': videos
    }

#########search box############
@get('/search-result')
def search_box(request,*,search):
    key_word='%%'+search+'%%'               ## %%是%的转义
    key_word='name like '+'\''+key_word+'\''
    blogs = yield from Blog.findAll(key_word, orderBy='created_at desc')
    audios = yield from AudioList.findAll(key_word, orderBy='created_at desc')
    videos = yield from VideoList.findAll(key_word, orderBy='created_at desc')
    return {
        '__template__': 'search.html',
        'blogs': blogs,
        'audios': audios,
        'videos': videos,
        'key_word': search
    }
