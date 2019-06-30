################################    URLLIB MODULE ##########################
import urllib.request
import urllib.response
import urllib.error
import urllib.parse


# GET request without headers
#url_data = urllib.request.urlopen("https://en.wikipedia.org")
#print(url_data.read())


#POST request without headers but with query string
try:
    url = 'https://www.google.com/search'
    values = {'q':'Python Programming Tutorials'}
    data = urllib.parse.urlencode(values)
    print(data)
    data = data.encode('utf-8')
    print(data)
    req = urllib.request.Request(url,data)
    print(req.get_full_url())
    url_data = urllib.request.urlopen(req)
    response = url_data.read()
    print(response)
except Exception as e:
    print(str(e))


#POST request with headers


try:
    url = 'http://www.pythonprogramming.net'
    values = {'s': 'Machine Learning',
              'submit': 'Search'
              }
    headers = dict()
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data,headers=headers)
    resp = urllib.request.urlopen(req)
    data_fetched = resp.read()
    filename = open("data.html","wb")
    filename.write(data_fetched)
    filename.close()

except Exception as e:
    print(str(e))

