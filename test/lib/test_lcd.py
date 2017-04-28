from __future__ import print_function
from reactionspeedgame.lib.lcd import Lcd
import unittest


class LcdTestCase(unittest.TestCase):
    lcd = None

    def setUp(self):
        self.lcd = Lcd()

    def test__init__(self):
        self.assertIsInstance(self.lcd, Lcd)

    def test_print(self):
        self.assertIs(self.lcd.print('test message', self.lcd.LINE_1), None)
        self.assertIs(self.lcd.print('test message', self.lcd.LINE_2), None)

    def test_clear(self):
        self.assertIs(self.lcd.clear(), None)

    def test_cleanup(self):
        self.assertIs(self.lcd.cleanup(), None)

    def test__exit__(self):
        self.assertIs(self.lcd.__exit__(), None)


if __name__ == '__main__':
    unittest.main()
