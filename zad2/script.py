import argparse
from pathlib import Path
import logging

from Game import Game
from Meadow import Meadow

start = True
parser = argparse.ArgumentParser(description='Herzlich willkommen', add_help=False)

parser.add_argument('-c', '--config', metavar='FILE', type=Path)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-l', '--log', metavar='LEVEL', type=int)
parser.add_argument('-r', '--rounds', metavar='NUM ', type=int)
parser.add_argument('-s', '--sheep', metavar='NUM ', type=int)
parser.add_argument('-w', '--wait', action='store_true')

args = parser.parse_args()
if args.config is not None:
    with open(args.config, 'r') as file:
        if file is None:
            raise 'File not found'
        print(file.read())
        file.close()

if args.help:
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
    start = False

if args.log is not None:
    with open('chasing.log', 'w') as file:
        file.write("test")
        file.close()

if args.rounds is not None:
    if args.rounds < 1:
        raise 'Rounds number must be greater than 0'
    else:
        Game.maxRounds = args.rounds

if args.sheep is not None:
    if args.sheep < 1:
        raise 'Sheep number must be greater than 0'
    else:
        Meadow.sheepQuantity = args.sheep
if args.wait:
    Game.break_after_round = True

if start:
    gra = Game()
    gra.run()
