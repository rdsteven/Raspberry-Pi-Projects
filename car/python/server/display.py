import time
from lib import LCD1602
import netifaces
import commands

class Display:
    def __init__(self):
        LCD1602.init(0x27, 1)

    def displayIP(self):
        iface = netifaces.ifaddresses('wlan0')
        self.message(0, iface[netifaces.AF_INET][0]['addr'])
	self.message(1, commands.getstatusoutput('iwgetid -r')[1])        
    def message(self, line, msg):
        LCD1602.write(0, line, msg)
