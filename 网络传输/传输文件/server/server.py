import socket,os
import subprocess
import struct,json

share_dir=r'D:\python3.7\chengxu\luffy\ch-5\联系网络传输\传输文件\server'
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)##让服务端尽可能快的回收端口
phone.bind(('127.0.0.1',8088))
# phone.listen(5)

while 1:#链接循环
    conn, addr = phone.accept()  #
    print('///',addr)
    while 1:#通信循环
        try:
            data=conn.recv(1024)
            print('对方输入>>',data)

            ##解析命令，提取命令参数
            cmds=data.decode('utf-8').split()
            file_name=cmds[1]
            ##以读的方式打开文件，读取文件的结果
            header_dic={
                'filename':file_name,
                'filemd5':'agrgr',
                'filesize':os.path.getsize('%s\%s'%(share_dir,file_name))
            }
            header_json=json.dumps(header_dic)
            header_bytes=header_json.encode('utf-8')
            header_size=struct.pack('i',len(header_bytes))##先发送报头的长度，再发报头，再发信息

            conn.send(header_bytes)
            # respond=input('回复》')

            ##发送真实的数据
            f=open('%s\%s'%(share_dir,file_name),'rb')
            for line in f:
                conn.send(line)


        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()
phone.close()