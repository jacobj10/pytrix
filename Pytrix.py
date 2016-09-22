class MatrixError(Exception):
	pass

class Matrix(object):
	def __init__(self, mat=None):
		same_len = True
		length = len(mat[0])
		for row in mat:
			if len(row) != length:
				same_len = False
		if not same_len:
			raise MatrixError, "The number of items in each row must be equal"
		self.rows = [row for row in mat]
		col_lst = []
		for col_index in range(len(mat[0])):
			col_lst.append([row[col_index] for row in self.rows])
		self.cols = col_lst
		self.mat = mat
		self.rank = (len(self.rows), len(self.cols))

	def __repr__(self):
		matrix = self.mat
		string = ""
		for row in matrix:
			string += " ".join([str(x) for x in row]) + "\n"
		return string

	def addRow(self, new_row, i = None):
		if len(new_row) != self.rank[1]:
			raise MatrixError, "The new row must be the same length as the other rows"
		if i == None:
			i = self.rank[0]
		self.mat.insert(i, new_row)


	def __add__(self, matrixB):
		if type(matrixB) != Matrix:
			raise MatrixError, "Addition is only defined between two matrices of equal length"
		if self.rank != matrixB.rank:
			raise MatrixError, "The matrices must be of equal rank"
		new_matrix = Matrix(self.mat)
		#for row in new_matrix.rows:
	
