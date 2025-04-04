'''解释：
UDP就像寄明信片，而TCP像打电话。

打电话（TCP）需要先拨号、等对方接听、确认身份后才能开始聊天，整个过程有来有往。而寄明信片（UDP）是你直接写好内容扔进邮筒，不管对方能不能收到，也不会确认对方是否真的收到了。

虽然理论上收发明信片的双方都是平等的，但通常我们把固定地址收明信片的一方叫"服务端"（比如网站服务器），主动寄出明信片的一方叫"客户端"（比如你的手机）。其实区别就在于谁在固定位置等着收件，谁在主动发件而已，不像打电话必须双方同时在线确认。
于是，UDP通信分为服务端和客户端，服务端固定地址，客户端不固定地址。
所以，UDP通信可以结合多线程的方式来实现双向自由通信'''


from socket import *
from threading import Thread

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 定义地址
addr = ('127.0.0.1', 8000)

# 绑定地址
udp_socket.bind(addr)

#不停接受信息
def receive_data():
    while True:
        # 接收数据,最大长度1024字节
        receivedata = udp_socket.recvfrom(1024)
        print(f"收到数据:{receivedata[0].decode('gbk')},from{receivedata[1]}")
        if receivedata[0] == '##':
            break

#不停发送
def send_data():
    while True:
        data = input('请输入要发送的数据:')
        udp_socket.sendto(data.encode('gbk'), addr)
        if data == '##':
            break

#创建线程
t1=Thread(target=receive_data)
t2=Thread(target=send_data) 


#启动
if __name__ == '__main__':
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    udp_socket.close()