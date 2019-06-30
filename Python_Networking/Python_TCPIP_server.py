import socket

host = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(5)

c, addr = s.accept()
print("Connected: ", addr)

c.send(b"Hello how are u there?")
msg = "and now i m saying bye!!!"
c.send(msg.encode())

c.close()





