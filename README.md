# Simple Chess Engine

This is a basic chess engine implemented in Python using the `chess` library. It utilizes the minimax algorithm with alpha-beta pruning for move selection.

![Image of a chessboard](https://github.com/Cassini-chris/simple_chess/blob/main/simple_chess.png)
<img src="[simple_chess/simple_chess.png](https://github.com/Cassini-chris/simple_chess/blob/main/simple_chess.png)" width="300"> 


## Features

* **Minimax Algorithm:**  The engine uses a minimax algorithm with a fixed depth search to determine the best move.
* **Alpha-Beta Pruning:**  Implements alpha-beta pruning to optimize the search process and reduce the number of nodes evaluated.
* **Simple Evaluation:**  The evaluation function currently only considers material value.
* **User Interface:**  Provides a basic command-line interface for playing against the engine.

## Getting Started

1. **Install the `chess` library:**
   ```bash
   pip install chess

## How to Play
The engine will print the board state.
Enter your move in UCI format (e.g., "e2e4", "a7a8q").
The engine will calculate its move and update the board.
Continue playing until the game ends.

## Limitations
Fixed Depth: The search depth is currently fixed. A deeper search would improve the engine's strength but require more processing time.
Basic Evaluation: The evaluation function is very simple and only considers material. A more sophisticated evaluation function would take into account positional factors, king safety, etc.
No Quiescence Search: The engine doesn't implement quiescence search, which can lead to "horizon effect" where it misses tactical opportunities.
