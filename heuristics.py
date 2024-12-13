def base_heuristic(current_game):
    board = current_game.get_grid()
    rows = len(board)
    cols = len(board[0])

    p1 = 1
    p2 = 2

    # Function to yield all lines (rows, columns, diagonals)
    def get_lines():
        # Rows
        for r in range(rows):
            yield board[r]
        # Columns
        for c in range(cols):
            yield [board[r][c] for r in range(rows)]
        # Main diagonals (\ direction)
        for start in range(-rows+1, cols):
            diag = []
            for r in range(rows):
                c = start + r
                if 0 <= c < cols:
                    diag.append(board[r][c])
            if len(diag) > 0:
                yield diag
        # Anti-diagonals (/ direction)
        for start in range(cols + rows - 1):
            diag = []
            for r in range(rows):
                c = start - r
                if 0 <= c < cols:
                    diag.append(board[r][c])
            if len(diag) > 0:
                yield diag

    def count_runs(line, player):
        runs_3 = 0
        runs_4 = 0
        length_line = len(line)
        i = 0
        while i < length_line:
            if line[i] == player:
                # Find the run of the same player
                j = i + 1
                while j < length_line and line[j] == player:
                    j += 1
                run_length = j - i

                # Check for run_length == 3
                if run_length == 3:
                    left_open = (i > 0 and line[i-1] == 0)
                    right_open = (j < length_line and line[j] == 0)
                    if left_open and right_open:
                        runs_3 += 1

                # Check for run_length == 4
                if run_length == 4:
                    left_open = (i > 0 and line[i-1] == 0)
                    right_open = (j < length_line and line[j] == 0)
                    if left_open or right_open:
                        runs_4 += 1

                i = j
            else:
                i += 1
        return runs_3, runs_4

    p1_score = 0
    p2_score = 0
    for line in get_lines():
        p1_3, p1_4 = count_runs(line, p1)
        p2_3, p2_4 = count_runs(line, p2)
        p1_score += (p1_3 + p1_4)
        p2_score += (p2_3 + p2_4)

    return p1_score - p2_score
