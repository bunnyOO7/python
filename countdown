import sys
import time
n=int(input(" enter the  time "))

def run(n):
    t=n/3600
    p=n%3600
    m=p/60
    s=p%60
    sys.stdout.write(f"\r{int(t)}:{int(m)}:{int(s)}")
    sys.stdout.flush()
    
while True:
    time.sleep(1)
    n=n-1
    run(n)
    if n==0:
        break
