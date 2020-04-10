import getch
import time
import sys
import threading



def watch():
    c=time.time()
    m=h=0
    while True:
        time.sleep(1)
        t=int(time.time()-c)
        if t>60:
            c=time.time()
            t=0
            m=m+1
        if m>60:
            m=0
            h=h+1
        sys.stdout.write(f"\r{h}:{m}:{t}")
        sys.stdout.flush()


def out():
    while True:
        c=input()
        if c:
            break





b=threading.Thread(target=watch,daemon=True)

a=threading.Thread(target=out)


b.start()
a.start()
a.join()
