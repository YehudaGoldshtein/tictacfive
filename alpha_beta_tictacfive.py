import math


def alphabeta_max(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = alphabeta_min(move, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        if v >= beta:
            return v, best_move
        alpha = max(alpha, v)
    return v, best_move

def alphabeta_min(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = alphabeta_max(move, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
        if v <= alpha:
            return v, best_move
        beta = min(beta, v)
    return v, best_move


def maximin(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move)
        if v < mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move


def minimax(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move)
        if v > mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move
