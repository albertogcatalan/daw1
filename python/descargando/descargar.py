# -*- coding: utf-8 -*-

'''
Created on 19/02/2012

@author: Alberto
'''
import urllib2

req = urllib2.urlopen('http://24.media.tumblr.com/avatar_374cb6a282fe_64.png')
CHUNK = 16 * 1024
with open('avatar_374cb6a282fe_64.png', 'wb') as fp:
    while True:
        chunk = req.read(CHUNK)
        if not chunk: break
        fp.write(chunk)