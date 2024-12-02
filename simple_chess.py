import chess
import random

def evaluate_board(board):
  """
  A simple evaluation function that scores the board based on material.
  """
  piece_values = {
      chess.PAWN: 1,
      chess.KNIGHT: 3,
      chess.BISHOP: 3,
      chess.ROOK: 5,
      chess.QUEEN: 9,
      chess.KING: 0  # King has infinite value, not relevant for material count
  }
  score = 0
  for piece_type in piece_values:
    score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
    score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
  return score

def get_random_move(board):
  """
  Returns a random legal move.
  """
  legal_moves = list(board.legal_moves)
  return random.choice(legal_moves)

def get_best_move(board, depth):
  """
  A simple minimax algorithm with a fixed depth.
  """
  best_score = -float('inf')
  best_move = None

  for move in board.legal_moves:
    board.push(move)
    score = -minimax(board, depth - 1, -float('inf'), float('inf'))
    board.pop()
    if score > best_score:
      best_score = score
      best_move = move

  return best_move

def minimax(board, depth, alpha, beta):
  """
  Recursive minimax helper function.
  """
  if depth == 0 or board.is_game_over():
    return evaluate_board(board)

  if board.turn == chess.WHITE:  # Maximizing player
    max_score = -float('inf')
    for move in board.legal_moves:
      board.push(move)
      score = minimax(board, depth - 1, alpha, beta)
      board.pop()
      max_score = max(score, max_score)
      alpha = max(alpha, score)
      if beta <= alpha:
        break
    return max_score
  else:  # Minimizing player
    min_score = float('inf')
    for move in board.legal_moves:
      board.push(move)
      score = minimax(board, depth - 1, alpha, beta)
      board.pop()
      min_score = min(score, min_score)
      beta = min(beta, score)
      if beta <= alpha:
        break
    return min_score

# Initialize the board
board = chess.Board()

# Play a game against the engine
while not board.is_game_over():
  print(board)
  if board.turn == chess.WHITE:
    # Player's turn
    move = input("Enter your move: ")
    try:
      move = chess.Move.from_uci(move)
      if move in board.legal_moves:
        board.push(move)
      else:
        print("Illegal move.")
    except:
      print("Invalid move format.")
  else:
    # Engine's turn
    print("Engine is thinking...")
    engine_move = get_best_move(board, depth=3)  # Adjust depth as needed
    board.push(engine_move)

# Print the game result
print(board)
if board.is_checkmate():
  print("Checkmate!")
elif board.is_stalemate():
  print("Stalemate.")
elif board.is_insufficient_material():
  print("Draw due to insufficient material.")
else:
  print("Draw.")
