# 处理多个客户端发送过来的连接请求，与接收消息
from socket import *
from threading import Thread


def handle_client_request(client_socket, client_addr):
    print(f"接受到：{client_addr},发送来{client_socket.recv(1024).decode('gbk')}")

if __name__ == '__main__':
    # 创建tcp_socket对象
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    # 设置端口复用，程序退出，端口号立即释放
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    # 绑定端口
    # 客户端可以通过这个端口号来找到我们这个服务器的tcp_socket服务
    ip_port = ('127.0.0.1', 8080)
    tcp_socket.bind(ip_port)
    # 设置监听:
    tcp_socket.listen(128)
    while True:
        # 分配对客户端的服务
        client_socket, client_addr = tcp_socket.accept()
        t1 = Thread(target=handle_client_request, args=(client_socket, client_addr))
        # t1.setDaemon(True)  # 设置守护线程
        # 启动线程
        t1.start()

