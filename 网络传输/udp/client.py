import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    msg=input('>>>')
    if not msg:continue
    phone.sendto(msg.encode('utf-8'),('127.0.0.1',8088))
    back_msg,addr=phone.recvfrom(1024)
    print(back_msg.decode('utf-8'),addr)