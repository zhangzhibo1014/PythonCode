import serial
ser = serial.Serial('COM4', 9600, timeout=1)

result=ser.write("我是东小东".encode("gbk"))
print("写总字节数:",result)
ser.close()