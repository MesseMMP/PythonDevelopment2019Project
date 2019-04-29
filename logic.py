import doctest

def one_step(matrix):
	'''
	>>> one_step([[0,0,0,0],[0,1,1,1],[0,0,1,0],[0,0,0,0]])
	[[0, 0, 1, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]

	>>> one_step([[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,0]])
	[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

	'''
	columns = len(matrix[0])
	rows = len(matrix)
	new_matrix = [[0 for i in range(columns)] for j in range(rows)]
	for row, row_cells in enumerate(matrix):
		for col, cell in enumerate(row_cells): 
			num_life = 0
			if row:
				if col:
					num_life += 1 if matrix[row-1][col-1] else 0
				if col < columns-1:
					num_life += 1 if matrix[row-1][col+1] else 0
				num_life += 1 if matrix[row-1][col] else 0
			if col:
				if row < rows-1:
					num_life += 1 if matrix[row+1][col-1] else 0
				num_life += 1 if matrix[row][col-1] else 0
			if row < rows-1:
				num_life += 1 if matrix[row+1][col] else 0
				if col < columns-1: 
					num_life += 1 if matrix[row+1][col+1] else 0
			if col < columns-1:
				num_life += 1 if matrix[row][col+1] else 0
			if cell:
				if num_life == 2 or num_life == 3:
					new_matrix[row][col] = 1
				else:
					new_matrix[row][col] = 0
			else:
				if num_life == 3:
					new_matrix[row][col] = 1
				else:
					new_matrix[row][col] = 0
	return new_matrix


if __name__ == '__main__':
	doctest.testmod()

'''
matrix = [[0,0,0,0],[0,1,1,1],[0,0,1,0],[0,0,0,0]]
print(one_step(matrix))
'''