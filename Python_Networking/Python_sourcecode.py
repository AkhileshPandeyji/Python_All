import urllib.request
import urllib.error

try:
    url = "http://pythonprogramming.net:80/beginner-python-programming-tutorials/"
    http = urllib.request.urlopen(url)
    print(http.read())

except urllib.error.HTTPError as e:
    print(str(e))
