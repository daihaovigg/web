#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Flask, request, render_template,url_for,redirect
from static.md5 import mymd5
from static.captcha import mycaptcha

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return render_template('welcome.html',back_url=url_for('static',filename='back.jpg'))


@app.route('/signin', methods=['GET'])
def signin_form():
  captcha=mycaptcha()
  captcha.save()
  return render_template('form.html',back_url=url_for('static',filename='back.jpg'),code_url=url_for('static',filename='code.jpg'))

@app.route('/code.jpg')
def capcode():
    redirect(url_for('static',filename='code.jpg',code=301))

@app.route('/back.jpg')
def background():
    redirect(url_for('static',filename='back.jpg',code=301))
    

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    #code = request.form['code']
    if username=='admin' and password=='password' :
#and code == captcha.code:
      usrinfo=mymd5(username,password)
      return redirect(url_for('home'))
    return render_template('form.html', message='Bad username or password', username=username,code_url=url_for('static',filename='code.jpg'))

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') #host=0.0.0.0 支持外网访问


