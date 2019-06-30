import socket

host = 'localhost'
port = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

    s.bind((host, port))
    s.settimeout(5)
    while True:
        msg, addr = s.recvfrom(1024)
        if msg is None:
            break
        print("Message Received:", str(msg.decode()), "From:", addr)

except socket.timeout as e:
    print("Server is disconnected")

s.close()
