import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return _heuristic(current_game), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        val, _ = alphabeta_min_h(move, _heuristic, depth - 1, alpha, beta)
        if val > v:
            v = val
            best_move = move
        if v >= beta:
            return v, best_move
        alpha = max(alpha, v)
    return v, best_move

def alphabeta_min_h(current_game, _heuristic, depth, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
         return current_game.get_score(), None
    if depth == 0:
        return  _heuristic(current_game), None

    v = math.inf

    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        val, _ = alphabeta_max_h(move, _heuristic, depth - 1, alpha, beta)
        if val < v:
            v = val
            best_move = move
        if v <= alpha:
            return v, best_move
        beta = min(beta, v)
    return v, best_move



def maximin(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1)
        if v < mx:
            v = mx
            best_move = move
    return v, best_move


def minimax(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1)
        if v > mx:
            v = mx
            best_move = move

    return v, best_move
