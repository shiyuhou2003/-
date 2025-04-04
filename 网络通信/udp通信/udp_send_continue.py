#UDP持续发送请求

#引入模块
from socket import *

#创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

#发送目标地址
udp_send_addr = ('127.0.0.1',8001)
while True:
#发送内容
    send_data = input('请输入发送的内容')

    #发送数据
    udp_socket.sendto(send_data.encode('gbk'),udp_send_addr)
    if send_data == '##':
        print('结束聊天')
        break
#关闭套接字
udp_socket.close()