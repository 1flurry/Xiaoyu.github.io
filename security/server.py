import os
import socket
import hashlib
import threading
import time
import struct
import ssl
import sqlite3

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
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from '+str(addr)+' closed')


    

class FileServer:
    def __init__(self):
        self.dataFormat = '20s20s8s32s100s100sl'
        self.cafile = "./cert/ca.crt"
        self.certfile = "./cert/server.pem"
        #soketlen_t clie_len

    def struct_pack(self):
        ret = struct.pack(self.dataFormat, self.username.encode(), self.pwd.encode(), self.action.encode(), self.md5sum.encode(), self.clientfilePath.encode(),
                          self.serverfilePath.encode(), self.size)
        return ret
 
    def struct_unpack(self, package):
        self.username, self.pwd, self.action, self.md5sum, self.clientfilePath, self.serverfilePath, self.size = struct.unpack(self.dataFormat, package)
        self.username = self.username.decode().strip('\x00')
        self.pwd = self.pwd.decode().strip('\x00')
        self.action = self.action.decode().strip('\x00')
        self.md5sum = self.md5sum.decode().strip('\x00')
        self.clientfilePath = self.clientfilePath.decode().strip('\x00')
        self.serverfilePath = self.serverfilePath.decode().strip('\x00')

    def CheckUsers(self,sock,addr):
        fileinfo_size = struct.calcsize(self.dataFormat)
        self.buf = sock.recv(fileinfo_size)
        if self.buf:
            self.struct_unpack(self.buf)
        name = self.username
        pwd = self.pwd
        print(name,pwd)

        conn   = sqlite3.connect('admin_db.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT PASSWORD from admin where ID = ?",list(name))
        for row in cursor:
            if pwd == row[0]:
                sock.send(b'1')
                filelist = self.GetFileList()
                sock.send(filelist.encode())
                self.FileSave(sock, addr)

            else:
                sock.send(b'0')
                print("error")
                '''
                sock.close()
                print('Connection from {0} closed.'.format(addr))
                conn.close()
                '''
                return 0

    def GetFileList(self):
        files= os.listdir("./server_data")
        return ",".join(files)

    def GetMD5(self,filepath):
        fd = open(filepath,"r")
        fcont = fd.readlines()
        fd.close()
        fmd5 = hashlib.md5(str(fcont).encode("utf-8"))
        return fmd5.hexdigest()    

    def FileSave(self,sock,addr):
        print ('Accept new connection from {0}'.format(addr))
        while True:
            fileinfo_size = struct.calcsize(self.dataFormat)
            self.buf = sock.recv(fileinfo_size)
            if self.buf:
                self.struct_unpack(self.buf)
                print(self.action)

                if self.action.startswith("upload"):
                    if os.path.isdir(self.serverfilePath):
                        fileName = (os.path.split(self.clientfilePath))[1]
                        self.serverfilePath = os.path.join(self.serverfilePath, fileName)
                    filePath,fileName = os.path.split(self.serverfilePath)
                    if not os.path.exists(filePath):
                        sock.send(str.encode('dirNotExist'))
                    else:
                        sock.send(str.encode('ok'))
                        recvd_size = 0
                        file = open(self.serverfilePath, 'wb')
                        while not recvd_size == self.size:
                            if self.size - recvd_size > 1024:
                                rdata = sock.recv(1024)
                                recvd_size += len(rdata)
                            else:
                                rdata = sock.recv(self.size - recvd_size)
                                recvd_size = self.size
                            file.write(rdata)
                        file.close()
                        output = self.GetMD5(self.serverfilePath)
                        if output == self.md5sum:
                            sock.send(str.encode('ok'))
                        else:
                            sock.send(str.encode('md5sum error'))

                elif self.action.startswith("download"):
                    filePath,fileName = os.path.split(self.serverfilePath)
                    print(self.serverfilePath)
                    if os.path.exists(filePath):
                        self.md5sum = self.GetMD5(self.serverfilePath)
                        self.action = 'ok'
                        self.size = os.stat(self.serverfilePath).st_size
                        ret = self.struct_pack()
                        sock.send(ret)
                        fo = open(self.serverfilePath, 'rb')
                        while True:
                            filedata = fo.read(1024)
                            if not filedata:
                                break
                            sock.send(filedata)
                        fo.close()
                    else:
                        self.action = 'nofile'
                        ret = self.struct_pack()
                        sock.send(ret)
            
            sock.close()
            print('Connection from {0} closed.'.format(addr))
            break


    def server(self):
        maxclientnum = InitMaxClientNum()
        server_port = 9999
        host = InitHost()

        purpose = ssl.Purpose.CLIENT_AUTH
        context = ssl.create_default_context(purpose, cafile=self.cafile)
        context.load_cert_chain(self.certfile)

        try:
            socketfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print(socketfd)
        except:
            print("Socket Build Error!")
        else:
            socketfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                socketfd.bind((host,server_port))
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

                        ssl_sock = context.wrap_socket(sock, server_side=True)
                        t1 = threading.Thread(target=self.CheckUsers, args=(ssl_sock, addr))
                        t1.start()
                        



if __name__ == '__main__':
    test = FileServer()
    test.server()
    #test.server()
