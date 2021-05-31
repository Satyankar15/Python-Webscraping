
  
import urllib.request as ur
import xml.etree.ElementTree as et

url =' http://py4e-data.dr-chuck.net/comments_202697.xml'

sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum=sum+int(count.text)

print('Sum:', sum)

