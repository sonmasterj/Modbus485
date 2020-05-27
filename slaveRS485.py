import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import time  
from modbus_tk import utils
import readDB
import configparser

# doc gia tri config cho database va serial, modBus
config = configparser.ConfigParser()
config.read('config.ini')

portSerial = config['Serial']['PORT']
baudrateSerial = int(config['Serial']['Baudrate'])

numD = int(config['Database']['NumDigital'])
numA = int(config['Database']['NumAnalog'])
url = config['Database']['URL']

slaveAdr = int(config['ModBus485']['SlaveAdr'])

# tao doi tuong database
db=readDB.ReadDB(numA,numD,url)

# tao doi duong modBus
modbusServ = modbus_rtu.RtuServer(serial.Serial(portSerial), baudrate= baudrateSerial,  
                  bytesize=8, parity='N', stopbits=1, xonxoff=0)
# start modBus
modbusServ.start()
# tao slave 
slave = modbusServ.add_slave(slaveAdr)
# tao memory cho slave vs doc regs: bat dau dia chi 0, co numA thanh ghi
slave.add_block( "1", modbus_tk.defines.HOLDING_REGISTERS, 0, numA)
# tao memory cho slave vs doc coils: bat dau dia chi 0, co numD thanh ghi
slave.add_block("2", modbus_tk.defines.COILS, 0, numD)

# slave_1.set_values("1",0,aa)
print("start")
while True:
    db.updateData()
    slave.set_values('1', 0, db.regData)
    slave.set_values('2', 0, db.coilData)
    time.sleep(5)