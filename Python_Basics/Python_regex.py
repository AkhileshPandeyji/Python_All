import re
import urllib.request
import urllib.parse

x = ''' John is 12 years old and Mike is 8 years old and Ben is 34 years 
        old and Martin is 123 years old
     '''

ages = re.findall(r'\d{1,3}',x)
names = re.findall(r'\W([A-Z][a-z]*)',x)

print(ages)
print(names)

parseResult = {}
x = 0
for person in names:
    parseResult[person]=ages[x]
    x+=1


print(parseResult)


try:
    url = "https://www.pythonprogramming.net"
    values ={'s':'Basics',
             'submit':'Search'
            }
    headers ={}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data,headers=headers)
    res = urllib.request.urlopen(req)
    filename = open("data_site.txt","w")
    x = str(res.read())
    data_site = re.findall(r'<p>(.*?)</p>',x)
    for eachdata in data_site:
        filename.write(eachdata+"\n")
    filename.close()
except Exception as e:
    print(str(e))







