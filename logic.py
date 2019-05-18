def one_step_life_dead(matrix):
    """Processing of one step with the return of the life and dead lists and
    area matrix
    """
    columns = len(matrix[0])
    rows = len(matrix)
    life_list = []
    dead_list = []
    new_matrix = [[0 for i in range(columns)] for j in range(rows)]
    for row, row_cells in enumerate(matrix):
        for col, cell in enumerate(row_cells):
            num_life = 0
            if row:
                if col:
                    num_life += 1 if matrix[row - 1][col - 1] else 0
                if col < columns - 1:
                    num_life += 1 if matrix[row - 1][col + 1] else 0
                num_life += 1 if matrix[row - 1][col] else 0
            if col:
                if row < rows - 1:
                    num_life += 1 if matrix[row + 1][col - 1] else 0
                num_life += 1 if matrix[row][col - 1] else 0
            if row < rows - 1:
                num_life += 1 if matrix[row + 1][col] else 0
                if col < columns - 1:
                    num_life += 1 if matrix[row + 1][col + 1] else 0
            if col < columns - 1:
                num_life += 1 if matrix[row][col + 1] else 0
            if cell:
                if num_life == 2 or num_life == 3:
                    new_matrix[row][col] = 1
                else:
                    new_matrix[row][col] = 0
                    dead_list.append((row, col))
            else:
                if num_life == 3:
                    new_matrix[row][col] = 1
                    life_list.append((row, col))
                else:
                    new_matrix[row][col] = 0
    return life_list, dead_list, new_matrix
