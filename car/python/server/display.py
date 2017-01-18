import time
from lib import LCD1602
import netifaces

class Display:
    def __init__(self):
        LCD1602.init(0x27, 1)

    def displayIP(self):
        iface = netifaces.ifaddresses('wlan0')
        self.message("IP: " + iface[netifaces.AF_INET][0]['addr'])
        # iwgetid -r to get network name

    def message(msg):
        LCD1602.write(0, 0, msg)
