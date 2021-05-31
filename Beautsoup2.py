# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:56:51 2020

@author: satya
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen( 'http://py4e-data.dr-chuck.net/known_by_Rholmark.html', context=ctx).read()


count=0

soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for line in tags:
    line.decode()
    count=count+1
    tag=line.get("href")
    print(tag)
    if(count==18):
        count=0
        name=line.contents[0]
        print(name)
        html = urlopen(tag, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags=soup('a')
        
