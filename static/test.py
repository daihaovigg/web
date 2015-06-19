#!/usr/bin/env python
#-*-coding:utf-8-*-

from captcha import mycaptcha
s=mycaptcha()
print s.code
s.reload()
s.save()
