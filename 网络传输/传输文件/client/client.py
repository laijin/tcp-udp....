import socket,struct,json


download_dir=r'D:\python3.7\chengxu\luffy\ch-5\联系网络传输\传输文件\client\download'
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8088))
while 1:
    msg=input('输入信息>>')  #get a.txt
    if not msg:continue
    phone.send(msg.encode('utf-8'))

    ##接收文件的内容，以写的方式打开

    obj=phone.recv(4)
    header_size=struct.unpack('i',obj)[0]##先接收报头的长度，再收报头，最后接收真实数据

    header_bytes=phone.recv(header_size)

    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    file_size=header_dic['file_size']
    file_name=header_dic['file_name']

    f = open('%s\%s' % (download_dir, file_name), 'wb')
    recv_size=0
    while recv_size<file_size:
        this_data=phone.recv(1024)
        f.write(this_data)
        recv_size+=len(this_data)
phone.close()