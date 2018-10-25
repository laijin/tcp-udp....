import socket
import subprocess
import struct,json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)##让服务端尽可能快的回收端口
phone.bind(('127.0.0.1',8088))
phone.listen(5)

while 1:#链接循环
    conn, addr = phone.accept()
    print('///',addr)
    while 1:#通信循环
        try:
            data=conn.recv(1024)
            print('对方输入>>',data)

            obj=subprocess.Popen(data.decode('GBK'),shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            header_dic={
                'filename':'a.txt',
                'filemd5':'agrgr',
                'filesize':len(stdout)+len(stderr)
            }
            header_json=json.dumps(header_dic)
            header_bytes=header_json.encode('utf-8')
            header_size=struct.pack('i',len(header_bytes))##先发送报头的长度，再发报头，再发信息

            conn.send(header_bytes)
            # respond=input('回复》')
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError: #适用于windows操作系统
            break