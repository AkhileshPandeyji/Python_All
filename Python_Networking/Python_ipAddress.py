import socket

try:
    urls = ["www.google.co.in", "www.python.org", "www.pythonprogramming.net", "www.google.com"]

    ip = []
    for url in urls:
        ip.append(socket.gethostbyname(url))

    for i in ip:
        print(i)

except socket.gaierror:
    print('There is no such address')


