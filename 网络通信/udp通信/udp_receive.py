from socket import *

#创建套接字对象
udp_socket = socket(AF_INET,SOCK_DGRAM) 

#绑定套接字本地端口
udp_socket.bind(('127.0.0.1',8000))

print("等待接收数据!")

#设置最大接收数据大小（本次接受最大的字节数）
receive_data = udp_socket.recvfrom(1024)

print(receive_data)

#如果是中文需要进行转码，否则报错

print(receive_data[0].decode('gbk'),{'127.0.0.1',8000})

udp_socket.close()