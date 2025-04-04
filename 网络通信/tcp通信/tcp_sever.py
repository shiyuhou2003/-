#tcp服务器开发

from socket import *

#创建套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
#设置端口号复用，程序退出时端口号立即释放
tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

tcp_socket.bind(('127.0.0.1', 8000))
#设置监听：128为最大等待的连接数
tcp_socket.listen(128)

#若有客户端连接，则产生一个新的套接字，用于后续通信
client_socket, client_addr = tcp_socket.accept()

#接收客户端发送过来的数据
recv_data = client_socket.recv(1024)
print(f"客户端发来:{recv_data.decode('gbk')}")

#发送数据给客户端
client_socket.send(input('请输入要发送到数据').encode('gbk'))

#关闭套接字
client_socket.close()
tcp_socket.close()