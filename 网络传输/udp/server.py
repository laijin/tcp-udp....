import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
phone.bind(('127.0.0.1',8088))
while 1:
    conn,addr=phone.recvfrom(1024)
    print(addr)
    phone.sendto(conn.upper(),addr)