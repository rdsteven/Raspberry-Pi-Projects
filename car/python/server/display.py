import time
import LCD1602
import netifaces

class Display:
    def __init__(self):
        LCD1602.init(0x27, 1)

    def displayIP():
        iface = netifaces.ifaddresses('en0')
        LCD1602.write(0, 0, "IP: " + iface[netifaces.AF_INET].addr)
