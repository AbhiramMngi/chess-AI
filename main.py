import numpy as np
from engine.engine import ChessEngine
import pyspiel
from chess import Board, Move
from constants import GAME

import chess.pgn as pgn


board = Board()
game = pyspiel.load_game(GAME).new_initial_state()



engine = ChessEngine({
   "Debug Log File": "",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 2, # More threads will make the engine stronger, but should be kept at less than the number of logical processors on your computer.
    "Ponder": "false",
    "Hash": 512, # Default size is 16 MB. It's recommended that you increase this value, but keep it as some power of 2. E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
    "MultiPV": 1,
    "Skill Level": 15,
    "Move Overhead": 10,
    "Minimum Thinking Time": 20,
    "Slow Mover": 100,
    "UCI_Chess960": "false",
    "UCI_LimitStrength": "false",
    "UCI_Elo": 2000,
}, depth = 10
)

while not game.is_terminal():
  action = np.random.choice(game.legal_actions(game.current_player()))

  san_move = game.action_to_string(game.current_player(), action)
  game.apply_action(action)

  uci_move = board.uci(board.parse_san(san_move))
  board.push_uci(uci_move)


  next_move_uci, reward = engine.make_best_move(uci_move)
  
  # print(reward)

  next_move_san = board.san(board.parse_uci(next_move_uci))
  board.push_uci(next_move_uci)

  game.apply_action(game.string_to_action(next_move_san))

game_pgn = pgn.Game().from_board(board=board)

print(game_pgn, file=open("test.pgn", "w"), end ="\n\n")



  



