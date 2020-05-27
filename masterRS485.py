import serial
import time
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# PORT = "COM6"
PORT = '/dev/ttyUSB1'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")
    master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0),
            t0=1
        )
        # master.set_timeout(0.5)
    master.set_verbose(True)
    logger.info("connected")
    while True:
        print("********************************new request*****************************************")
        try:
            logger.info(master.execute(2, cst.READ_HOLDING_REGISTERS,1,2))
        except modbus_tk.modbus.ModbusError as exc:
            logger.error("%s- Code=%d", exc, exc.get_exception_code())
        time.sleep(1)
        print("\n\r")

if __name__ == "__main__":
    main()