import numpy as np

from open_spiel.python.algorithms import mcts
from engine.engine import ChessEngine
import copy

class StockFishEvaluator(mcts.Evaluator):
  """An AlphaZero MCTS Evaluator."""

  def __init__(self, config={},depth=10):
    self.engine = ChessEngine(config=config,depth=depth)

  def evaluate(self, state):
    value = self.engine.evaluate(state)
    return np.array([value, -value])

  def prior(self, state):
    action_values = []
    
    for action in state.legal_actions():
      new_state = copy.deepcopy(state)
      new_state.apply_action(action)
      action_values.append(self.evaluate(new_state))

    action_values = np.array(action_values)

    policy =  action_values / action_values.sum()

    return [(action_values[i], policy[i])for i in len(state.legal_actions())]
  
    
