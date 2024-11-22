import random
import math
import PIL.Image

class Pont():
    a: int
    b: int
    def __init__(self,a,b):
        self.a=a
        self.b=b

def tavolsag(x1,x2,y1,y2):
    dx=(x1/w)-(x2/w)
    dy=(y1/h)-(y2/h)
    v=int(255*math.sqrt(dx**2+dy**2))
    return v

s=20
w=400
h=400
o=0
pontok: list[Pont]=[]
    
kep = PIL.Image.new(size=(w, h), mode="RGB") 

for i in range(s):
    pontok.append(Pont(random.randint(0,w),random.randint(0,h)))

for x in range(w):
    for y in range(h):
        tavolsagok=[]
        for pont in pontok:
            tavolsagok.append(tavolsag(pont.a,x,pont.b,y))
        tavolsagok.sort()
        v=tavolsagok[o]
        pixelszin = (v,v,v)
        kep.putpixel((x, y),pixelszin)

kep.show()
kep.save("kep.png")
