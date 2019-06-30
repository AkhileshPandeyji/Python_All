import socket

host = 'localhost'
port = 7600

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

filename = input("Enter The Filename: ")

s.send(filename.encode())

contents = s.recv(1024)

while contents:
    print(str(contents.decode()))
    file = open("Downloads/{}".format(filename), 'wb')
    file.write(contents)
    contents = s.recv(1024)

s.close()
