import requests
import regex
from os import system 
import time
 


session=requests.session()

response1=session.get("http://ip138.com/")
html1=response1.text

reg1=r"<iframe src=\"(http:\/\/[\S]+)\" [\s\S]+>[\s\S]*<\/iframe>"

pattern1=regex.compile(reg1)

url=pattern1.findall(html1)
response2=session.get(url[0])
html2=response2.text
reg2=r"<title>您的IP地址是：([\S]+)<\/title>"

pattern2=regex.compile(reg2)

ip=pattern2.findall(html2)


with open('ip.txt','w') as f:
    f.write(ip[0])
	
	
system('git add .')
system('git commit -m %s' % time.strftime("%Y%m%d%H%M%S", time.localtime()))
system('git push origin master')
