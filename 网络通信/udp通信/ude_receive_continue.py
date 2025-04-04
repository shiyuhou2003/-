from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)
#绑定地址
udp_socket.bind(('127.0.0.1',8001))
print('等待接收数据')

while True:
    #接收数据
    receive_data = udp_socket.recvfrom(1024)
    #打印接收到的数据
    print(receive_data[0].decode('gbk'),{'127.0.0.1',8001})
    if receive_data[0].decode('gbk') == '##':
        break
#关闭套接字
udp_socket.close()