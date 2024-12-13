import numpy as np
def get_sequences_as_strings(grid):
    strings = []
    rows, cols = grid.shape
    for i in range(rows):
        strings.append(''.join(str(x) for x in grid[i, :]))
    for i in range(cols):
        strings.append(''.join(str(x) for x in grid[:, i]))
    for i in range(rows):
        strings.append(''.join(str(x) for x in grid.diagonal(i)))
        strings.append(''.join(str(x) for x in np.fliplr(grid).diagonal(i)))
    return strings

def get_all_sequences(grid, player, length):
    #return sequences of length 'length' that contain only 'player' in the grid that has a zero before or after the sequence
    #sequences can be horizontal, vertical or diagonal
    other_player = 1 if player == 2 else 2
    p1_moves, p2_moves = 0, 0
    strings = get_sequences_as_strings(grid)
    string_formats_for_player = {str(player) * length + '0', '0' + str(player) * length}
    string_formats_for_other_player = {str(other_player) * length + '0', '0' + str(other_player) * length}
    for string in strings:
        if string in string_formats_for_player:
            p1_moves += 1
        if string in string_formats_for_other_player:
            p2_moves += 1
    return p1_moves - p2_moves


def base_heuristic(curr_state):
    grid = curr_state.get_grid()
    player = curr_state.get_curr_player()
    return get_all_sequences(grid, player, curr_state.winning_length)

def advanced_heuristic(curr_state):
    return base_heuristic(curr_state)
