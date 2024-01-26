import serial

# Taking input from serial port /dev/ttyACM0
arduinoData = serial.Serial('/dev/ttyACM0', 115200)

# main loop
while True:
    #taking input from user ex. Temp, Humidity
    cmd = input('What measurement do you want? ')
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())
    while arduinoData.inWaiting() == 0:
        pass
    dataPacket = arduinoData.readline()
    dataPacketc = str(dataPacket, 'UTF-8')
    dataPacket = dataPacket.strip('\r\n')
    print(dataPacket)
    splitPacket = dataPacket.split(':')
    if splitPacket[0] == "Temp":
        print('The Temperature is: ', float(splitPacket[1]), 'Degrees F')
    if splitPacket[0] == "Humidity":
        print('The Humidity is: ', float(splitPacket[1]), '% Humidity')