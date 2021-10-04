import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import datetime
import startTime
import threading
import time
import RPi.GPIO as GPIO

global chan1
global chan2 
global volt_output_0_degree = 500*10**(-3)
global temp_coefficient = 10**(-3)
global runtime_interval = 10 #By default
global runcount = 0 #Counter for runtime interval incrementations
global btn_toggle = 37

def setup():
    global chan1
    global chan2
    global startTime
    global btn_toggle

    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pins 1 & 2
    chan1 = AnalogIn(mcp, MCP.P1) #Temperature
    chan2 = AnalogIn(mcp, MCP.P2) #Brightness

    #Button set up
    GPIO.setup(btn_toggle, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    #Debouncing
    GPIO.add_event_detect(btn_toggle, GPIO.FALLING, callback=btn_toggle_rate(), bouncetime=200)
   
    #Start timing
    startTime = time.time()
    #pass

def fetch_sensor_vals():
    global chan1
    global chan2
    global startTime
    global volt_output_0_degree
    global temp_coefficient
    global runtime_interval
    
    #threading
    thread = threading.Timer(runtime_interval, fetch_sensor_vals)
    thread.daemon = True
    thread.start()
    
    # Fetches the sensor values.
    timeNow = time.time()
    
    #print out values
    tempOut = (chan1.voltage - volt_output_0_degree)/temp_coefficient
    print(round(timeNow-starTime), 's \t \t', chan1.value, '\t \t \t', round((tempOut),1) , 'C' , '\t',chan2.value)
    #pass

def btn_toggle_rate(root_path):   #COULD BE WRONG PARAMETR
    global runtime_interval
    global runcount
    if runcount == 0:
        runtime_interval = 5
        runcount = (runcount+1)%3
    elif runcount == 1:
        runtime_interval = 1
        runcount = (runcount+1)%3
    elif runcount == 2:
        runtime_interval = 10
        runcount = (runcount+1)%3
    #pass

if __name__ == "__main__":
    setup()
    print('Runtime \t Temp Reading \t \t Temp \t \t Light Reading')
    fetch_sensor_vals()
    while True:
        pass    #Run forever and ever, Amen
      




