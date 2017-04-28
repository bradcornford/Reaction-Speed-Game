from __future__ import print_function
from reactionspeedgame.lib.game import Game
import time
import unittest


class GameTestCase(unittest.TestCase):
    LEDS = ()

    SWITCHES = ()

    COUNTDOWN = 0

    GAME_TIME = 0

    SCORE_INCREMENT = 1

    game = None

    def setUp(self):
        self.game = Game(self.LEDS, self.SWITCHES, self.COUNTDOWN, self.GAME_TIME, self.SCORE_INCREMENT)

    def test__init__(self):
        self.assertIsInstance(self.game, Game)

    def test_start(self):
        self.game.GAME_TIME = 2
        self.assertIs(self.game.start(True), None)

    def test_get_score(self):
        self.assertIs(self.game.get_score(), 0)

    def test_print_information(self):
        self.game.FINISH_TIME = time.time()
        self.assertIs(self.game.print_information(), None)

    def test_print_score(self):
        self.assertIs(self.game.print_score(), None)
        self.assertIs(self.game.print_score(True), None)

    def test_flash_buttons(self):
        self.assertIs(self.game.flash_buttons(self.game.BUTTON_ACTION_ALL), None)
        self.assertIs(self.game.flash_buttons(self.game.BUTTON_ACTION_SNAKE), None)

    def test_finish(self):
        self.assertIs(self.game.finish(), None)

    def test_reset(self):
        self.assertIs(self.game.reset(), None)

    def test_cleanup(self):
        self.assertIs(self.game.cleanup(), None)

    def test__exit__(self):
        self.assertIs(self.game.__exit__(), None)


if __name__ == '__main__':
    unittest.main()
