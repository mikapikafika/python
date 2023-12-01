from Game import Game
from Meadow import Meadow
import configparser

from Sheep import Sheep
from Wolf import Wolf


def help_message():
    print("This program simulates a wolf chasing sheep in a meadow.\n")
    print("The program takes the following arguments:")
    print("-c, --conf FILE where FILE is a path to a configuration file. ")
    print("-h, --help to display this help message.")
    print("-l, --log LEVEL where LEVEL is a logging level.")
    print("-r, --rounds NUM where NUM is a number of rounds that will be "
          "played. ")
    print("-s, --sheep NUM where NUM is a number of sheep that will be "
          "placed in the meadow. ")
    print("-w, --wait to wait for pressing any key after each round.\n")


def rounds_number(number):
    if number < 1:
        raise 'Rounds number must be greater than 0'
    else:
        Game.maxRounds = number


def sheep_number(number):
    if number < 1:
        raise 'Sheep number must be greater than 0'
    else:
        Meadow.sheepQuantity = number


def load_config(path):
    with open(path, "r") as file:
        config = configparser.ConfigParser()
        config.read_file(file)
        Sheep.InitPosLimit = float(config["Sheep"]["InitPosLimit"])
        Sheep.move_distance = float(config["Sheep"]["MoveDist"])
        Wolf.move_distance = float(config["Wolf"]["MoveDist"])
