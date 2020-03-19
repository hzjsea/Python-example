import socket

# 建立连接 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.python.org',80))
# 当连接完成，套接字可以用来发送请求来接收页面上显示的文字。
# 同样是这个套接字也会用来读取响应，最后再被销毁。是的，被销毁了。客户端套接字通常用来做一次交换（或者说一小组序列的交换）