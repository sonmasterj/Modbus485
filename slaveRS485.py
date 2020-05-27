import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import time  
from modbus_tk import utils
import readDB
import configparser
numA=7
numD=4
url = 'http://localhost:5000/'
db=readDB.ReadDB(numA,numD,url)
modbusServ = modbus_rtu.RtuServer(serial.Serial('/dev/ttyUSB0'), baudrate= 9600,  
                  bytesize=8, parity='N', stopbits=1, xonxoff=0)
print("start")
modbusServ.set_verbose(True)
modbusServ.start()
slave_1 = modbusServ.add_slave(2)
# # modbusServ._do_run()
slave_1.add_block( "1", modbus_tk.defines.HOLDING_REGISTERS, 0, 7)
# aa = (1000,2000,3000,4000,5000) # data in the register
# # # modbusServ._do_run()
# slave_1.set_values("1",0,aa)


while True:
    db.updateData()
    slave_1.set_values('1',0,db.regData)
    time.sleep(5)