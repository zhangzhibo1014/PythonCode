import serial

serialPort = "COM4"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))


while 1:
    str = ser.readline()
    print(str)

ser.close()