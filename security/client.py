import socket
import hashlib
import os
import struct
import ssl,argparse

def InitHost():
    host = ""
    with open("./host.txt","r") as fd:
        n2 = fd.readlines()
        for n in n2:
            return n






class FileClient():
    def __init__(self):
        self.action = ''
        self.fileName = ''
        self.md5sum = ''
        self.clientfilePath = ''
        self.serverfilePath = ''
        self.size = 0
        self.cafile = "./cert/ca.crt"
        self.host = InitHost()
        self.server_port = 9999
        self.dataFormat='20s20s8s32s100s100sl'

    def struct_pack(self):
        ret = struct.pack(self.dataFormat, self.username.encode(), self.pwd.encode(), self.action.encode(), self.md5sum.encode(), self.clientfilePath.encode(),
                          self.serverfilePath.encode(), self.size)
        return ret

    def struct_unpack(self,package):
        self.username, self.pwd, self.action, self.md5sum, self.clientfilePath, self.serverfilePath, self.size = struct.unpack(self.dataFormat, package)
        self.username = self.username.decode().strip('\x00')
        self.pwd = self.pwd.decode().strip('\x00')
        self.action = self.action.decode().strip('\x00')
        self.md5sum = self.md5sum.decode().strip('\x00')
        self.clientfilePath = self.clientfilePath.decode().strip('\x00')
        self.serverfilePath = self.serverfilePath.decode().strip('\x00')
    
    def CheckUsers(self,name,pwd):
        self.ClientLink()
        
        self.username = name
        self.pwd = pwd
        ret = self.struct_pack()
        self.s.send(ret)
        recv = self.s.recv(1024)
        if recv.decode() == '0':
            print("id or pwd error!")
            return 0
        else:
            filelist = self.s.recv(1024).decode().split(",")
            print(filelist)
            return 1


    def GetMD5(self,filepath):
        fd = open(filepath,"r")
        fcont = fd.readlines()
        fd.close()
        fmd5 = hashlib.md5(str(fcont).encode("utf-8"))
        return fmd5.hexdigest()    
        
    def ClientLink(self):
        purpose = ssl.Purpose.SERVER_AUTH
        self.context = ssl.create_default_context(purpose, cafile=self.cafile)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = InitHost()
        server_port = 9999
        self.sock.connect((host, server_port))
        self.s = self.context.wrap_socket(self.sock, server_hostname=self.host)

    def SendFile(self,clientfilePath,serverfilePath):
        if not os.path.exists(clientfilePath):
            print('源文件/文件夹不存在')
            return "No such file or directory"
        self.action = 'upload'
        self.md5sum = self.GetMD5(clientfilePath)
        self.size = os.stat(clientfilePath).st_size
        self.serverfilePath = os.path.basename(serverfilePath)
        self.clientfilePath = os.path.basename(clientfilePath)
        ret = self.struct_pack()

        
        try:
            #self.ClientLink()
            s = self.s
            s.send(ret)
            recv = s.recv(1024)
            if recv.decode() == 'dirNotExist':
                print("目标文件/文件夹不存在")
                return "No such file or directory"
            elif recv.decode() == 'ok':
                fo = open(clientfilePath, 'rb')
                while True:
                    filedata = fo.read(1024)
                    if not filedata:
                        break
                    s.send(filedata)
                fo.close()
                recv = s.recv(1024)
                if recv.decode() == 'ok':
                    print("文件传输成功")
                    s.close()
                    return 0
                else:
                    s.close()
                    return "md5sum error:md5sum is not correct!"
        except Exception as e:
            print(e)

    def RecvFile(self,clientfilePath,serverfilePath):
        if not os.path.isdir(serverfilePath):
            filePath,fileName = os.path.split(serverfilePath)
        else:
            filePath = serverfilePath
        if not os.path.exists(clientfilePath):
            print('本地目标文件/文件夹不存在')
            return "No such file or directory"
        self.action = 'download'
        self.serverfilePath = serverfilePath
        self.clientfilePath = clientfilePath
        ret = self.struct_pack()
        
        try:
            host = InitHost()
            server_port = 9999
            #self.ClientLink()
            s = self.context.wrap_socket(self.sock, server_hostname=host)
            s.send(ret)
            recv = s.recv(struct.calcsize(dataFormat))
            self.struct_unpack(recv)
            if self.action.startswith("ok"):
                if os.path.isdir(clientfilePath):
                    fileName = (os.path.split(serverfilePath))[1]
                    clientfile = os.path.join(clientfilePath, fileName)
                self.recvd_size = 0
                file = open(clientfile, 'wb')
                while not self.recvd_size == self.size:
                    if self.size - self.recvd_size > 1024:
                        rdata = s.recv(1024)
                        self.recvd_size += len(rdata)
                    else:
                        rdata = s.recv(self.size - self.recvd_size)
                        self.recvd_size = self.size
                    file.write(rdata)
                file.close()
                print('\n等待校验...')
                output = self.GetMD5(clientfile)
                if output == self.md5sum:
                    print("文件传输成功")
                else:
                    print("文件校验不通过")
                    (status, output) = subprocess.getstatusoutput("del " + clientfilePath)
            elif self.action.startswith("nofile"):
                print('远程源文件/文件夹不存在')
                return "No such file or directory"
        except Exception as e:
            print(e)




    
    

if __name__ == '__main__':
    fileclient = FileClient()
    fileclient.CheckUsers("1","123456")
    fileclient.SendFile('./client_data/test.txt','./server_data')
    #fileclient.RecvFile('./client_data/','./server_data/test2.txt')
