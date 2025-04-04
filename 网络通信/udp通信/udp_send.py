from socket import *
#   *代表导入socket中的所有模块

udp_socket = socket(AF_INET,SOCK_DGRAM) #创建套接字

#数据发送的地址
udp_send_addr = ('127.0.0.1',8000) #发送的地址ip和端口

# 发送的内容
send_data = '111222333'

#发送数据
udp_socket.sendto(send_data.encode('gbk'),udp_send_addr)

#关闭套接字
udp_socket.close()