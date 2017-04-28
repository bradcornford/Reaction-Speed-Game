from __future__ import print_function
from lib.game import Game
import atexit
import config


def main():
    game = Game(
        config.game['leds'],
        config.game['switches'],
        config.game['countdown'],
        config.game['game_time'],
        config.game['score_increment']
    )

    game.start()

    atexit.register(game.__exit__)


if __name__ == '__main__':
    main()
