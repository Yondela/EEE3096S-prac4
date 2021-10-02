import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import threading
import time
import RPi.GPIO as GPIO

runtime_interval = [10, 5, 1]
current_runtime_interval = 0
btn_toggle = 37


volt_output_0_degree = 500*10**(-3)
temp_coefficient = 10**(-3)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)

def setup():
    # This setup has to handle the button that changes the values
    #GPIO.setmode(GPIO.BOARD)

    #GPIO.setup(btn_toggle, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #GPIO.add_event_detect(btn_toggle, GPIO.FALLING, callback=btn_toggle_rate(), bouncetime=200)
    pass

def fetch_sensor_vals():
    # Fetches the sensor values.
    #print("Raw ADC Value: ", chan0.value)
    #print("ADC Voltage: " + str(chan0.voltage) + "V")
    print("Raw ADC Value: ", chan1.value)
    print("ADC Voltage: " + str(chan1.voltage) + "V")
    #time.sleep(runtime_interval[current_runtime_interval])

    #temp = (float(chan1.voltage)-volt_output_0_degree)/(temp_coefficient)
    #print("{}, {}, {} C, {}".format(10, chan1.value, temp, chan0.value))
    time.sleep(1)
    #pass

def btn_toggle_rate(channel):
    # You need to make this run on it's own thread so that when the button
    # is pressed it will change the rate.
    #current_runtime_interval += 1
    #current_runtime_interval %= 3
    pass


##print("Raw ADC Value: ", chan.value)
##print("ADC Voltage: " + str(chan.voltage) + "V")


# create an analog input channel on pin 1
##chan = AnalogIn(mcp, MCP.P1)
##print("Raw ADC Value: ", chan.value)
##print("ADC Voltage: " + str(chan.voltage) + "V")

if __name__ == "__main__":

    try:
        #setup()
        #print(1)
        print("Runtime     Temp Reading     Temp    Light Reading")
        while True:
            fetch_sensor_vals()
    except Exception as e:
        print(e)
        #GPIO.cleanup()
    #finally:
        #GPIO.cleanup()




