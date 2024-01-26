import serial.tools.list_ports



ports = serial.tools.list_ports.comports()

serial_inst = serial.Serial()



ports_list = []



for port in ports:

    ports_list.append(str(port))

    print(str(port))



val = input('Select Port: ')



for i in range(len(ports_list)):

    if ports_list[i].startswith(f'COM{val}'):

        port_var = f'{val}'

        print(port_var)


port_var = f'{val}'
serial_inst.baudrate = 9600

serial_inst.port = port_var

serial_inst.open()



while True:

    command: str = input('Arduino Command: (ON/OFF): ').upper()

    print(command)

    serial_inst.write(command.encode('utf-8'))



    if command == 'EXIT':

        exit(0)