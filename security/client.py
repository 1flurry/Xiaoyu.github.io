import socket

def InitHost():
    host = ""
    with open("./host.txt","r") as fd:
        n2 = fd.readlines()
        for n in n2:
            return n

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    host = InitHost()
    s.connect((host, 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
	
	client()
