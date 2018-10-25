import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8088))
while 1:
    msg=input('输入信息>>')
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print('--',data)



