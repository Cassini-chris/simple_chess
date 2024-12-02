# Simple Chess Engine

This is a basic chess engine implemented in Python using the `chess` library. It utilizes the minimax algorithm with alpha-beta pruning for move selection.

## Features

* **Minimax Algorithm:**  The engine uses a minimax algorithm with a fixed depth search to determine the best move.
* **Alpha-Beta Pruning:**  Implements alpha-beta pruning to optimize the search process and reduce the number of nodes evaluated.
* **Simple Evaluation:**  The evaluation function currently only considers material value.
* **User Interface:**  Provides a basic command-line interface for playing against the engine.

## Getting Started

1. **Install the `chess` library:**
   ```bash
   pip install chess
