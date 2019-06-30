import socket
import time
host = 'localhost'
port = 6000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

time.sleep(5)

s.sendto(b"Hello How are u there I am fine here",(host,port))

msg = "Now I am saying bye!!!!!"

s.sendto(msg.encode(),(host,port))

s.close()

