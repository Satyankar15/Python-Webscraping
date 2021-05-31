# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:47:35 2020

@author: satya
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0

html = urlopen( 'http://py4e-data.dr-chuck.net/comments_202695.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#
spans = soup('span')
for line in spans:
    line.decode()
    sum=sum+int(line.contents[0])
print(sum)