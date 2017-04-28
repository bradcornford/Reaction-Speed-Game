from __future__ import print_function
import reactionspeedgame.main
import unittest


class MainTestCase(unittest.TestCase):
    def test__init__(self):
        self.assertTrue("main" in dir(reactionspeedgame.main))
