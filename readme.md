# Chess AI

A Reinforcement Learning agent to play chess by adapting to the Stockfish engine.

The aim of this project is to learn the **Stockfish**'s heuristic evaluation function which can be used as a value function to evaluate states in a reinforcement learning system.

This evaluation function will then be used by a search algorithm like Monte Carlo Tree Search (as used in the project) to find optimal actions, i.e., optimal moves given a state of the board.

To learn the heuristic evaluation function of Stockfish, we've used the Neural network architecture used by the famous algorithm **AlphaZero**. The Implementation and the game environment is given to us by the library **open_spiel**.

The training strategy is to use self-play to improve the performance of the value function, i.e, The NN. 

