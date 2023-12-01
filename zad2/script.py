import argparse
from pathlib import Path
import logging

from Game import Game
from Meadow import Meadow


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-c', '--config', metavar='FILE', type=Path)
# parser.add_argument('-h', '--help')
parser.add_argument('-l', '--log', metavar='LEVEL', type=int)
parser.add_argument('-r', '--rounds', metavar='NUM ', type=int)
parser.add_argument('-s', '--sheep', metavar='NUM ', type=int)
parser.add_argument('-w', '--wait', action='store_true')

args = parser.parse_args()

if args.log is not None:
    with open('chasing.log', 'w') as file:
        file.write("test")
        file.close()

if args.config is not None:
    with open(args.config, 'r') as file:
        if file is None:
            raise 'File not found'
        print(file.read())
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
gra = Game()
gra.run()

