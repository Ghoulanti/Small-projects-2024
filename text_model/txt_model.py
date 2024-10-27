import random
from szolista import szolista

szo=input("valamit irj ide vagy idk: ")
szam=int(input("ennyi szoval folytassa: "))
szo=szo.split()

szo1=szo[-2]
szo2=szo[-1]

for i in range(szam):
    print(szo1,end=' ')
    szo3=random.choice(szolista[(szo1,szo2)])
    szo1,szo2=szo2,szo3
