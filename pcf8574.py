from smbus import SMBus
from termcolor import cprint
info="""
How it works?
1. Get a DEC value from addr (0-255)
2. Converts DEC to BIN with convert_dec2bin
3. Generates new byte for i2c (in bin)
4. Converts new byte to DEC value
5. Sends DEC to addr (0-255)
"""
logo="""
[]  []
[] []
[][]
[] []
[]  []
[]  []
Made by K4CZP3R @2016
"""

class control:
    def info(self):
        cprint(logo,'red')
    def __init__(self,bus,addr,clearbyte=1,debug=0):
        self.debug = debug
        self.printinfo(logo,2)
        self.printinfo("DEBUG MODE - ENABLED",2)
        self.bus = bus
        self.addr = addr
        self.printinfo("Bus = " + str(self.bus) +"\nAddress: " + str(self.addr) + " (Dec)",2)
        self.printinfo("[>] Setting up bus",0)
        self.bus = SMBus(self.bus)
        self.printinfo("    [!] Bus is ready",1)
        if clearbyte == 1:
            self.printinfo("[>] Sending byte to addr",0)
            self.bus.write_byte(self.addr,0xff)
            self.printinfo("    [!] Byte sended!",1)
        else:
            self.printinfo("[*] Omitting clear byte",2)
    def printinfo(self,what,clr):
        colors = ['yellow','green','cyan']
        if self.debug == 1:
            cprint(what,colors[clr])
    def convert_hex2bin(self,hexval):
        return bin(int(str(hexval),16))[2:].zfill(8)
    def convert_bin2dec(self,binval):
        return int(binval,2)
    def convert_dec2bin(self,dec):
        readed_dec = str(dec)
        readed_hex = str(hex(dec))
        readed_bin = self.convert_hex2bin(str(readed_hex)[2:])
        return readed_bin
    def generate_new_bin(self,abin,led):
        abin = int(abin)
        if led == 1:
            if str(abin).zfill(8)[7] == "1":
                command = abin - 1
            else:
                command = abin + 1
        elif led == 2:
            if str(abin).zfill(8)[6] == "1":
                command = abin - 10
            else:
                command = abin + 10
        elif led == 3:
            if str(abin).zfill(8)[5] == "1":
                command = abin - 100
            else:
                command = abin + 100
        elif led == 4:
            if str(abin).zfill(8)[4] == "1":
                command = abin - 1000
            else:
                command = abin + 1000
        elif led == 5:
            if str(abin).zfill(8)[3] == "1":
                command = abin - 10000
            else:
                command = abin + 10000
        elif led == 6:
            if str(abin).zfill(8)[2] == "1":
                command = abin - 100000
            else:
                command = abin + 100000
        elif led == 7:
            if str(abin).zfill(8)[1] == "1":
                command = abin - 1000000
            else:
                command = abin + 1000000
        elif led == 8:
            if str(abin).zfill(8)[0] == "1":
                command = abin - 10000000
            else:
                command = abin + 10000000
        else:
            cprint("Pin doesn't exist!, selecting 1","red")
            if str(abin).zfill(8)[7] == "1":
                command = abin - 1
            else:
                command = abin + 1
        return command
    def changestate(self,pin):
        actualbyte=self.bus.read_byte(self.addr)
        self.printinfo("[*] Raw dec from bus is: " + str(actualbyte),2)
        self.printinfo("[>] Converting dec to bin...",0)
        actualbin=self.convert_dec2bin(actualbyte)
        self.printinfo("    [!] Converted bin looks like: " + str(actualbin),1)
        self.printinfo("[>] Generating bin to on/off pin " + str(pin),0)
        cmd=self.generate_new_bin(actualbin,pin)
        self.printinfo("    [!] Bin generated! (%s)" % str(cmd).zfill(8),1)
        self.printinfo("[>] Converting bin to dec",0)
        cmddec=self.convert_bin2dec(str(cmd))
        self.printinfo("    [!] Converted dec looks like: " + str(cmddec),1)
        self.printinfo("[>] Sending dec to bus",0)
        self.bus.write_byte(self.addr,int(cmddec))
        self.printinfo("    [!] Dec sended!",1)
