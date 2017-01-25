import Adafruit_BMP.BMP085 as BMP085
import time
import serial
import strftime from time
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0) #Open the serial Port
ser.flushInput()        # Clear the input buffer

#Recieve a line from the Arduberry and return it back
def receive():
  while True:
        state = ser.readline()
        if len(state):  #If something was read from the Serial Port, read and return$
                return state

#Send data to the Arduberry
def send(input):
        ser.write(input)
def setup():
        print '\n Barometer begins...'

def loop():
        while True:
                sensor = BMP085.BMP085()
                temp = sensor.read_temperature()        # Read temperature to veria$
                pressure = sensor.read_pressure()       # Read pressure to veriable$

                print ''
                print '      Temperature = {0:0.2f} C'.format(temp)             # P$
                print '      Pressure = {0:0.2f} Pa'.format(pressure)   # Print pre$
                time.sleep(1)
                print ''

def destory():
        GPIO.cleanup()                          # Release resource

while True:
        try:
                send('s')
                print receive(),
        except KeyboardInterrupt:       #If program is terminated, close the serial $
                ser.close()

if __name__ == '__main__':              # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:       # When 'Ctrl+C' is pressed, the child progr$
                destory()


