import time
import subprocess
import LCD1602

if __name__ == '__main__':
	LCD1602.init(0x27, 1)
	LCD1602.write(0, 0, 'test')
	time.sleep(2)
