import socket,struct,json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8088))
while 1:
    msg=input('输入信息>>')
    if not msg:continue
    phone.send(msg.encode('utf-8'))

    obj=phone.recv(4)
    header_size=struct.unpack('i',obj)[0]##先接收报头的长度，再收报头，最后接收真实数据

    header_bytes=phone.recv(header_size)

    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    file_size=header_dic['file_size']

    recv_size=0
    recv_data=b''
    while recv_size<file_size:
        this_data=phone.recv(1024)
        recv_size+=len(this_data)
    print('--',recv_data.decode('GBK'))
