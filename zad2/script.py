import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-c', '--config', metavar='FILE')
parser.add_argument('-h', '--help')
parser.add_argument('-l', '--log', metavar='LEVEL')
parser.add_argument('-r', '--rounds', metavar='NUM ', type=int)
parser.add_argument('-s', '--sheep', metavar='NUM ', type=int)
parser.add_argument('-w', '--wait')
args = parser.parse_args()
print(args.accumulate(args.integers))