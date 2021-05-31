# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:51:31 2020

@author: satya
"""

import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen('https://www.coursera.org/learn/python-network-data/lecture/kWTYV/worked-example-using-urllib-chapter-12')
for line in fhand:
    print(line.decode())