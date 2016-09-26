from Pytrix import Matrix, MatrixError

class SudoMatrix(Matrix):

	def transpose(self):
		row_num, col_num = self.rank
		new_rows = []
		for i in range(0, col_num):
			new_cols = []
			for j in range(0, row_num):
				new_cols.append(self.mat[j][i])
			new_rows.append(new_cols)
		return Matrix(new_rows)

