#!/usr/bin/python
#encoding:utf-8

import hashlib
from collections import defaultdict

class mymd5(object):
  def __init__(self,username,password):
    self.usr=username
    self.passwd=self.get_md5(password+'dai_blog')

  def get_md5(self,password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


