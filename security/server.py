import os
import socket
import signal
import asyncio
import aiohttp
import threading

def InitMaxClientNum():
    buf = ""
    with open("./maxclientnum.txt","r") as fd:
        nBytes=fd.readlines()
        for n in nBytes:
            if int(n) < 0:
                print("Data Error!(need > 0)")
                return -1
            return int(n)
    
def InitHost():
    host = ""
    with open("./host.txt","r") as fd:
        n2 = fd.readlines()
        for n in n2:
            return n

def tcplink(sock, addr):
    print('Accept new connection from ' ,addr)
    sock.send(b'Welcome!')
    '''while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))'''
    sock.close()
    print('Connection from %s closed.' % addr)

class MainThread:
    def  __init__(self):
        self.reuse = 1
        self.i = 0
        self.new_fd = 0
        self.tempsocke_fd = 0
        #soketlen_t clie_len

    def server(self):
        maxclientnum = InitMaxClientNum()
        server_port = socket.htons(maxclientnum)
        host = InitHost()
        try:
            socketfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print(socketfd)
        except:
            print("Socket Build Error!")
        else:
            socketfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                socketfd.bind((host,9999))
            except:
                print("Sokcet Bind Error!")
            else:
                try:
                    socketfd.listen(maxclientnum)
                except:
                    print("Socket Listen Error!")
                else:
                    print('Waiting for connection...')
                    while True:
                        # 接受一个新连接:
                        sock, addr = socketfd.accept()
                        # 创建新线程来处理TCP连接:
                        t = threading.Thread(target=tcplink, args=(sock, addr))
                        t.start()

if __name__ == '__main__':
    test = MainThread()
    test.server()
