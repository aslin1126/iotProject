from I2C_device import *
class Board:
    def __init__(self, addr=0x48, port=1):
        self.device = I2C_device(addr, port)
 
    def control(self):
        self.device.read_data(0x00)
        return self.device.read_data(0x00)
 
    def light(self):
        self.device.read_data(0x01)
        return self.device.read_data(0x01)
 
    def temperature(self):
        self.device.read_data(0x02)
        return self.device.read_data(0x02)
 
    def custom(self):
        self.device.read_data(0x03)
        return self.device.read_data(0x03)
 
    def output(self, val):
        self.device.write_cmd_arg(0x40, val)
 