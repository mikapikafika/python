import argparse
from pathlib import Path
from Script_Functions import *
from Game import Game


start = True

parser = argparse.ArgumentParser(description='Herzlich willkommen',
                                 add_help=False)

parser.add_argument('-c', '--config', metavar='FILE', type=Path)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-l', '--log', metavar='LEVEL', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
parser.add_argument('-r', '--rounds', metavar='NUM ', type=int)
parser.add_argument('-s', '--sheep', metavar='NUM ', type=int)
parser.add_argument('-w', '--wait', action='store_true')

args = parser.parse_args()

if args.config is not None:
    load_config(args.config)

if args.help:
    help_message()
    start = False

if args.log is not None:
    with open('chasing.log', 'w') as file:
        file.write("test")
        file.close()

if args.rounds is not None:
    rounds_number(args.rounds)

if args.sheep is not None:
    sheep_number(args.sheep)

if args.wait:
    Game.break_after_round = True

if start:
    gra = Game()
    gra.run()
