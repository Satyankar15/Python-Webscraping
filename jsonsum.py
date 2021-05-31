# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:21:32 2020

@author: satya
"""

import json
import urllib.request as ur

sum=0

url='http://py4e-data.dr-chuck.net/comments_202698.json'
site=ur.urlopen(url).read()

info=json.loads(site)
for item in info['comments']:
    sum=sum+int(item['count'])

print(sum)