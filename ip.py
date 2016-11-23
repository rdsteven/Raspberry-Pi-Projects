#!/usr/bin/env python
import time
import subprocess
import LCD1602

if __name__ == '__main__':
	LCD1602.init(0x27, 1)
	
	while True:
		ip = subprocess.check_output(['hostname', '-I']).strip('\n').strip()
		LCD1602.clear()
		
		if not ip:
			LCD1602.write(0, 0, "Starting Up")
			LCD1602.write(0, 1, "  Have a shot!")
		else:
			LCD1602.write(0, 0, ip)
		time.sleep(30)		
