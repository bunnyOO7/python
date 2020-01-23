#!/usr/bin/python3
import socket
import os
import time
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=8880
b=""
c.connect(('127.0.0.1',port))
start=time.time()
while 1 :
    now=time.time()-start
    o=c.recv(1024)
    g=o.decode()
    print("\n")
    print(f"server -> {g}")
    print("\n")
    d=input("client -> ")
    c.send(d.encode())
    if d=='eof':
        break

    if len(o)>0:
        f=open("chat.text",'a')
        f.write(f"server -> {g}\n")

        f.write(f"client -> {d}\n")
        f.close()
    if now>3:
        start=time.time()
        f=open("chat.text",'r')
        li=f.read().splitlines(True)
        f.close()
        li.pop(0)
        os.remove("chat.text")
        for i in li:
            j=open("chat.text",'a')
            j.write(i)
            j.close()
            
        os.system("clear")
        for i in li:
            if i==li[-1]:
                print(f"{i}",end="")
                continue
            print(f"{i}\n")
c.close()


