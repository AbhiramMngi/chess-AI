from stockfish import Stockfish
import os 
import numpy as np


class ChessEngine:
  def __init__(self, config={}, depth=10):
    self.engine = Stockfish(os.environ["STOCKFISH_PATH"], parameters=config, depth=depth)
  
  def set_position(self, position):
    self.engine.set_fen_position(position)
  
  
  def evaluate(self, state):
    eval = self.engine.set_fen_position(str(state)).get_evaluation()

    return eval["value"]

