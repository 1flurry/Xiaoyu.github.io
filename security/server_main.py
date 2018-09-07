import _thread
import time
import sys
import os
#import log
#import db_update
import sqlite3
import socket
import thread
MAX_THR_NUM = 100

class FilePackage:
    def __init__(self):
        self.cmd = ''
        self.filesize = 0
        self.ack = 0
        self.username = ''
        self.filename = ''
        #mode_t mode;        // 文件的权限
        self.buf = ''

class server:
    def __init__(self):
        self.cmd = ''
        self.filesize = 0
        self.ack = 0
        self.username = ''
        self.filename = ''
        #mode_t mode;        // 文件的权限
        self.buf = ''

    def InitMaxClientNum():
        buf = ""
        with open("./maxclientnum.txt","r") as fd:
            nBytes=fd.readlines()
            for n in nBytes:
                if int(n) < 0:
                    print("Data Error!(need > 0)")
                    return -1
                return int(n)

    #管理员身份认证模块
    def CheckAdmin(id,pwd):
        conn = sqlite3.connect('admin_db.db')
        cursor = conn.execute("SELECT PASSWORD  from admin where ID = ?",[id])
        for row in cursor:
            if pwd == row[0]:
                conn.close()
                return 1
            else:
                conn.close()
                return 0

    #管理员登录模块
    def login():
        flag = 0
        while flag != 1:
            print("Admin Id:")
            Adminid = input()
            print("Admin Password")
            Adminpwd = input()
            res = server.CheckAdmin(int(Adminid),Adminpwd)
            if res == 1:
                flag = 1
                print('login sucess!')
            else:
                print('login faile!')

def Process(CurrentClientNum):
    sendPackage = FilePackage()
    CurrentClientNum = CurrentClientNum + 1
    if CurrentClientNum > maxClientNum:
        sendPackage = pack('L'," "," ",0,2,1,"")
        CurrentClientNum = CurrentClientNum - 1
        return 0
    buff = FilePackage()
    

    

if __name__ == '__main__':
    maxClientNum = server.InitMaxClientNum()
    CurrentClientNum = 0
    print('Max Client Number is',maxClientNum)
    server.login()
    test = thread.MainThread()
    test.server()

    
'''
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
	#界面线程
    _thread.start_new_thread( print_time, ("ControId", 2, ) )
    #处理数据线程
    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print ("Error: 无法启动线程")
'''

