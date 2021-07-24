import time
import serial
import schedule
serial_port = serial.Serial(
	    port="/dev/ttyS0",
	    baudrate=9600,
	    bytesize=serial.EIGHTBITS,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_ONE,
	    )
# Wait a second to let the port initialize
time.sleep(1)
i =0
def API():

	f = open('/home/nvidia/API/hospitals-main/API_status.txt','r')
	print(f.read())
	if f.read() == "done":
		address = open('/home/nvidia/API/hospitals-main/hospitals.txt','r') 
		api = address.read()
		print(api)
		serial_port.write(api.encode())
		#f.truncate(0)
		#address.truncate(0)
		print("clear")
		

	f.close()
	
def camera():
	result_file = open('/home/nvidia/Camera/output.txt','r+')
	result_camera = result_file.read()
	print(result_camera)
	if  result_camera == "0":

		serial_port.write("violation of face mask".encode())
		serial_port.write("cough detected\r\n".encode())
def COVID():
	result_file = open('/home/nvidia/COVID/output.txt','r+')
	result_covid = result_file.read()
	serial_port.write("0".encode())
while i< 3 :
	API()
	camera()
	COVID()
	
	i= i +1
