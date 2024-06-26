from MCTs.MCTs import *
from MCTs.OthelloGame_for_MCTs import *
from Othello_Game import *
import argparse

parser = argparse.ArgumentParser(description="Specify the algorithms parameters.")
parser.add_argument("--search", type=int, default=1000, help="Searching and exploring the Game Space (Simulation)")

args = parser.parse_args()

othello = OthelloGame()
game = OthelloGAME()
mcts = MCTs(othello, args.search)

game.MinMax_vs_MCTs(mcts = mcts)