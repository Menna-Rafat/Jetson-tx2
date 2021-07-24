#!/usr/bin/python3
import time
import serial
import schedule

def uart():
	def read():

		data = serial_port.readline().decode()
		print(data)
		#serial_port.write(data)
	flag=1
	print(flag)


	serial_port = serial.Serial(
	    port="/dev/ttyS0",
	    baudrate=9600,
	    bytesize=serial.EIGHTBITS,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_ONE,
	    timeout  = 1000,
	    write_timeout  = None, 
	    inter_byte_timeout = None,
	    rtscts = True,)
	# Wait a second to let the port initialize
	time.sleep(1)

	try:
    # Send a simple header
	#f = open('hospitals.txt', 'r') 
	#file_contents = f.read()
		print("send")
	#while flag==  1:
		
	#	if serial_port.inWaiting() > 0:
	            #print("ready")	
	            #for i in  range(11):
	           	#read()
	 #           flag=0
	            #serial_port.close()	
		
			
	#print (file_contents)
	    #serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
		while flag==  1:
			if serial_port.inWaiting() > 1:
	           		print("ready")	
	           		for i in  range(11):
	            			read()
	           		flag=0
		serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
	    #        serial_port.close()
    #time.sleep(1)
	            # if we get a carriage return, add a line feed too
	            # \r is a carriage return; \n is a line feed
	            # This is to help the tty program on the other end 
	            # Windows is \r\n for carriage return, line feed
            # Macintosh and Linux use \n
	            #if data == "\r\n".encode():
	                # For Windows boxen on the other end
	                ##serial_port.write("\n".encode())


	except KeyboardInterrupt:
	    print("Exiting Program")

	except Exception as exception_error:
	 #   print("Error occurred. Exiting Program")
	    print("Error: " + str(exception_error))

	finally:
	
		serial_port.close()	
	    
	pass
#uart()
schedule.every(5).seconds.do(uart)
while 1:
	schedule.run_pending()
