#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Flask, request, render_template
from static.md5 import mymd5
from static.captcha import mycaptcha

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return render_template('welcome.html')

def home(name):
    user = { 'nickname': name } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("home.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/', methods=['REQUEST'])
def signin_form():
  captcha=mycaptcha()
  captcha.save()
  return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
      usrinfo=mymd5(username,password)
      return home(usrinfo.usr)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0') #host=0.0.0.0 支持外网访问


