#!/usr/bin/python3
# -*- coding: utf-8 -*-

# flask框架学习
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])
def siginfrom():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
if __name__ == '__main__':
    app.run()