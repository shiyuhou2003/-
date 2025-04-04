'''
TCP网络应用程序开发分为：
1.tcp客户端开发
2.tcp服务器开发
客户端是「我要什么」（主动索取），服务端是「你要什么我给你」（被动响应）。
也就是说，主动发起建立连接请求的是客户端程序，等待连接请求的是服务端程序

'''

# tcp客户端开发

from socket import *

# 创建套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
addr = ('127.0.0.1', 8000)
tcp_socket.connect(addr)
#发送数据
data = input('请输入要发送的数据：')
tcp_socket.send(data.encode('gbk'))

receive_data = tcp_socket.recv(1024)
print(f"接收到服务器发来的数据, {receive_data.decode('gbk')}")

# 关闭套接字
tcp_socket.close()