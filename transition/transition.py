from sunrise import *
from blinkt import *

def rgb(color):
   return str(color["r"])+","+str(color["g"])+","+str(color["b"])

def adjust(key, src,dest):
    diff = abs(src[key] - dest[key])
    adjusted = {"r":src["r"],"b":src["b"],"g":src["g"]}
    step = 1
    if(step > diff):
        step = diff
    if(diff > 0):
        if(src[key]<dest[key]):
            adjusted[key] = src[key]+ step
        if(src[key]>dest[key]):
            adjusted[key] = src[key]-step
    return adjusted
def key_equal(key,src,dest):
    return src[key]==dest[key]

def equal(src,dest):
    return key_equal("r",src,dest) and key_equal("g",src,dest) and key_equal("b",src,dest)

def move(start, end):
   while(equal(start,end)==False):
       start = adjust("r", start, end)
       start = adjust("g", start, end)
       start = adjust("b", start, end)

       for pixel in range(0,8):
           set_pixel(pixel,start["r"],start["g"],start["b"],0.2)

       show()

       print(rgb(start) + " " + rgb(end))
       if(start["r"] != end["r"]):
          print ("Red")
       if(start["g"] != end["g"]):
          print ("Green")
       if(start["b"] != end["b"]):
          print ("Blue")

for n in range(0, len(colors)):
    if(n != len(colors)-1):
        move(colors[n], colors[n+1])
    if(n == len(colors)):
        move(colors[n], colors[n])
