import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)##让服务端尽可能快的回收端口
phone.bind(('127.0.0.1',8088))
phone.listen(5)

while 1:
    conn, addr = phone.accept()
    print('///',addr)
    while 1:
        try:
            data=conn.recv(1024)
            print('对方输入>>',data)
            data=data.upper()
            # respond=input('回复》')
            conn.send(data)
        except ConnectionResetError: #适用于windows操作系统
            break
