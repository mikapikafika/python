from Game import Game
from Meadow import Meadow
import configparser
import logging
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

        init_poss = float(config["Sheep"]["InitPosLimit"])
        move_dis_sheep = float(config["Sheep"]["MoveDist"])
        move_dis_wolf = float(config["Wolf"]["MoveDist"])

        if init_poss < 0:
            raise 'initial position limit must be greater than 0'
        if move_dis_sheep < 0:
            raise 'sheep move distance must be greater than 0'
        if move_dis_wolf < 0:
            raise 'wolf move distance must be greater than 0'

        log_message = str("data from file loaded: init_pos_limit: " + str(
            init_poss) + ", sheep_move_dist: " + str(
            move_dis_sheep) + ", wolf_move_dist: " + str(move_dis_wolf))

        logging.debug('%s log_message %s', 'debug', log_message)
        Sheep.InitPosLimit = init_poss
        Sheep.move_distance = move_dis_sheep
        Wolf.move_distance = move_dis_wolf


def create_log_file(level):
    logging.basicConfig(filename='chasing.log',
                        format='%(levelname)s:%(message)s', level=level)
