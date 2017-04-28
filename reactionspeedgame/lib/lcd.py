from __future__ import print_function
from mock import MagicMock
import sys
import time


try:
    import smbus as Smbus
except ImportError:
    print("[Lcd][error] An error occurred importing 'smbus'")
    mock = MagicMock()
    mock.write_byte.return_value = True
    sys.modules['smbus'] = mock
    import smbus as Smbus


class Lcd:
    I2C_ADDRESS = 0x3f
    WIDTH = 16

    CHR = 1
    CMD = 0

    LINE_1 = 0x80
    LINE_2 = 0xC0
    LINE_3 = 0x94
    LINE_4 = 0xD4

    BACKLIGHT = 0x08

    ENABLE = 0b00000100

    E_PULSE = 0.0005
    E_DELAY = 0.0005

    smbus = None

    def __init__(self):
        print("[Lcd][info] Initialising LCD")

        self.smbus = Smbus.SMBus(1)

        try:
            self.__write(0x33, self.CMD)
            self.__write(0x32, self.CMD)
            self.__write(0x06, self.CMD)
            self.__write(0x0C, self.CMD)
            self.__write(0x28, self.CMD)
            self.__write(0x01, self.CMD)

            time.sleep(self.E_DELAY)
        except AttributeError:
            print("[Lcd][error] An error occurred initialising LCD")

    def __toggle_enabled_bits(self, bits):
        time.sleep(self.E_DELAY)
        self.smbus.write_byte(self.I2C_ADDRESS, (bits | self.ENABLE))
        time.sleep(self.E_PULSE)
        self.smbus.write_byte(self.I2C_ADDRESS, (bits & ~self.ENABLE))
        time.sleep(self.E_DELAY)

    def __write(self, bits, mode):
        bits_high = mode | (bits & 0xF0) | self.BACKLIGHT
        bits_low = mode | ((bits << 4) & 0xF0) | self.BACKLIGHT

        self.smbus.write_byte(self.I2C_ADDRESS, bits_high)
        self.__toggle_enabled_bits(bits_high)

        self.smbus.write_byte(self.I2C_ADDRESS, bits_low)
        self.__toggle_enabled_bits(bits_low)

    def print(self, message, line):
        print("[Lcd][info] Writing message: '%s' to LCD line decimal: '%d'" % (message, line))

        try:
            message = message.ljust(self.WIDTH, " ")

            self.__write(line, self.CMD)

            for i in range(self.WIDTH):
                self.__write(ord(message[i]), self.CHR)
        except AttributeError:
            print("[Lcd][error] An error occurred printing message on LCD")

    def clear(self):
        print("[Lcd][info] Clearing messages on LCD")

        try:
            self.__write(0x01, self.CMD)
        except AttributeError:
            print("[Lcd][error] An error occurred clearing message on LCD")

    def cleanup(self):
        print("[Lcd][info] LCD clean up")
        self.clear()

    def __exit__(self):
        print("[Lcd][info] Lcd exit")

        self.cleanup()
