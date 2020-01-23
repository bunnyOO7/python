#!/usr/bin/python3
import socket
import os
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=""
port=8880
s.bind((host,port))
s.listen(2)
conn,addr=s.accept()
start=time.time()
while 1 :

    now=time.time()-start
    print("\n")
    msg=input("server -> ")

    conn.send(msg.encode())
    o=conn.recv(1024)
    o.strip()
    if len(o)>0:
        g= o.decode()
        f=open("chatserver.text",'a')
        f.write(f"server -> {msg}\n")
        f.write(f"client -> {g}\n")

        f.close()
        print("\n")
        print("client -> " + g)
    if now>5:
        start=time.time()
        f=open("chatserver.text",'r')
        li=f.read().splitlines(True)
        f.close()
        li.pop(0)
        os.remove("chatserver.text")
        for i in li:
            j=open("chatserver.text",'a')
            j.write(i)
            j.close()

        os.system("clear")
        for i in li:
            if i==li[-1]:
                print(f"{i}",end="")
                continue
            print(f"{i}\n")
   
   
   
   
   
    if msg == 'eof':
         break
s.close()

