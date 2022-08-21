from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausem, sleep_us as pausau
led1  = pin(13,pin.OUT)
led2 = pin(12,pin.OUT)
led3 = pin(14,pin.OUT)
led4 = pin(27,pin.OUT)
led5 = pin(26,pin.OUT)
led6 = pin(25,pin.OUT)
led7 = pin(15,pin.OUT)
led8 = pin(2,pin.OUT)
led9 = pin(4,pin.OUT)
led10 = pin(5,pin.OUT)
 
puerto=[13, 12, 14, 27, 26, 25, 15, 2, 4, 5]
 
luces=[]
for i in puerto:
    luces.append (pin(i,pin.OUT))
print (luces)
def derecha():
    for i in luces:
        for j in range (2):
            i.value(not i.value())
        pausem(500)
def izquierda():
    for i in reversed (luces):
        for j in range (2):
          i.value(not i.value())
        pausem(500)
while True:
    derecha()
    izquierda()
