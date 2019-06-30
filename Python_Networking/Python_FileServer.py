import socket

host = 'localhost'
port = 7600

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

c, addr = s.accept()

filename = str(c.recv(1024).decode())

try:
    file = open(filename, "rb")
    contents = file.read()
    file.close()
    c.send(contents)
except FileNotFoundError as e:
    print(str(e))
    msg = filename + " :File Does Not Exist"
    s.send(b"File does not exist!!!!!!")
    s.send(msg.encode())

c.close()