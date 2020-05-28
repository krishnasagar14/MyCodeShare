class NQueenPuzzle(object):
	def __init__(self, n=8):
		self.n = n
		self.board = [[0 for i in range(n)] for i in range(n)]
		if self.solve_n_queens(0):
			self.__repr__()

	def is_conflict_in_current_pos(self, pos, col):
		for c in range(col):
			if self.board[pos][c] == 1:
				return True
		for r, c in zip(range(pos, -1, -1), range(col, -1, -1)):
			if self.board[r][c] == 1:
				return True
		for r, c in zip(range(pos, self.n), range(col, -1, -1)):
			if self.board[r][c] == 1:
				return True
		return False

	def solve_n_queens(self, col):
		if col >= self.n:
			return True
		for i in range(self.n):
			if not self.is_conflict_in_current_pos(i, col):
				self.board[i][col] = 1
				if self.solve_n_queens(col + 1):
					return True
				self.board[i][col] = 0
		return False

	def __repr__(self):
		print("Board:\n")
		for r in self.board:
			print(" ".join(map(str, r)) + "\n")

NQueenPuzzle(n=0)
NQueenPuzzle(n=1)
NQueenPuzzle(n=2)
NQueenPuzzle(n=3)
NQueenPuzzle(n=4)
NQueenPuzzle(n=5)
NQueenPuzzle()
