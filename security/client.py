import socket
import server_client
import hashlib
import os
import struct

def InitHost():
    host = ""
    with open("./host.txt","r") as fd:
        n2 = fd.readlines()
        for n in n2:
            return n

dataFormat='8s32s100s100sl'

class FileClient():
    def __init__(self):
        self.action = ''
        self.fileName = ''
        self.md5sum = ''
        self.clientfilePath = ''
        self.serverfilePath = ''
        self.size = 0

    def struct_pack(self):
        ret = struct.pack(dataFormat,self.action.encode(),self.md5sum.encode(),self.clientfilePath.encode(),
                          self.serverfilePath.encode(),self.size)
        return ret

    def struct_unpack(self,package):
        self.action,self.md5sum,self.clientfilePath,self.serverfilePath,self.size = struct.unpack(dataFormat,package)
        self.action = self.action.decode().strip('\x00')
        self.md5sum = self.md5sum.decode().strip('\x00')
        self.clientfilePath = self.clientfilePath.decode().strip('\x00')
        self.serverfilePath = self.serverfilePath.decode().strip('\x00')
    
    def GetMD5(self,filepath):
        fd = open(filepath,"r")
        fcont = fd.readlines()
        fd.close()
        fmd5 = hashlib.md5(str(fcont).encode("utf-8"))
        return fmd5.hexdigest()    
        
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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            host = InitHost()
            server_port = 9999
            s.connect((host, server_port))
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
        self.serverfilePath = os.path.basename(filePath)
        self.clientfilePath = os.path.basename(clientfilePath)
        ret = self.struct_pack()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            host = InitHost()
            server_port = 9999
            s.connect((host, server_port))
            s.send(ret)
            recv = s.recv(struct.calcsize(dataFormat))
            self.struct_unpack(recv)
            if self.action.startswith("ok"):
                if os.path.isdir(clientfilePath):
                    fileName = (os.path.split(serverfilePath))[1]
                    clientfile = os.path.join(clientfilePath, fileName)
                self.recvd_size = 0
                file = open(clientfilePath, 'wb')
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
                output = self.GetMD5(clientfilePath)
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
    fileclient.SendFile('./client_data/test.txt','./server_data')
    fileclient.RecvFile('./client_data/','./server_data/test2.txt')
