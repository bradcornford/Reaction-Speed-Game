# Raspberry Pi Python reaction speed game

A project to create a reaction speed game on a Raspberry Pi using GPIO / I2C.

## Requirements

This package requires the following system packages to be installed:

- python-dev
- build-essential
- python-pip
- python-smbus
- libi2c-dev 
- i2c-tools 
- libffi-dev

These can be installed using the following:

    sudo apt-get update
    sudo apt-get install -y python-dev build-essential python-pip python-smbus libi2c-dev i2c-tools libffi-dev

## Installation

Begin by installing this packages requirements:

    sudo -H pip install -e .
    
Finally copy the example configuration file `example.config.py`, and save it as `config.py`

    cp reactionspeedgame/example.config.py reactionspeedgame/config.py

## Configuration

You can now configure Reaction-Speed-Game in a few simple steps. Open `reactionspeedgame/config.py` and update the options as needed.

- `leds` - An array of LEDs using GPIO pin as the key.
- `switches` - An array of Switches using GPIO pin as the key.
- `countdown` - The game countdown in seconds.
- `game_time` - The game play time in seconds.
- `score_increment` - The number to increment score by in game.
    
## Usage

It's really as simple as using the Mapper class

    sudo python reactionspeedgame/main.py
    
### License

Reaction-Speed-Game is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT)
