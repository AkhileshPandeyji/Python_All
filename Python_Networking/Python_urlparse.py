import urllib.parse
import urllib.error

url = "http://pythonprogramming.net:80/beginner-python-programming-tutorials/"

try:
    tpl = urllib.parse.urlparse(url)

    print("Scheme:", tpl.scheme)
    print("Net Location:", tpl.netloc)
    print("Port:", tpl.port)
    print("Path:", tpl.path)
    print("Complete Url:", tpl.geturl())

except urllib.error.HTTPError as e:
    print(str(e))
