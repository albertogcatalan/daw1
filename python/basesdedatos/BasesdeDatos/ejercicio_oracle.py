# -*- coding: utf-8 -*-

'''
Created on 22/02/2012

@author: Alberto
'''

import cx_Oracle

con = cx_Oracle.connect('hr/case@127.0.0.1:8080/apex')
print con.version

con.close()