
import RPi.GPIO as GPIO
import time

# Pin Definitions
input_pin = 18  # BCM pin 18, BOARD pin 12

def main():
    prev_value = GPIO.LOW
    i = 0
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while i < 3 :
            value = GPIO.input(input_pin)
            
            if value != prev_value:
                if value == GPIO.LOW:
                   # f = open('/home/nvidia/API/hospitals-main/API_status.txt','r+') 
                    
                    
                  
      	              value_str = "LOW"
                else:
                    value_str = "HIGH"
                print("Value read from pin {} : {}".format(input_pin,
                                                           value_str))
                i= i+1
                prev_value = value
            time.sleep(1)
    finally:
        GPIO.cleanup()
#with open("file.txt", "r") as f:
 #   searchlines = f.readlines()
#for i, line in enumerate(searchlines):
 #   if "searchphrase" in line: 
 #       for l in searchlines[i:i+3]: print l,
 #       print

if __name__ == '__main__':
    main()
