class MatrixError(Exception):
	pass


class Matrix(object):
	def __init__(self, mat=None):
		if mat is None:
			mat = self.get_input()
		same_len = True
		length = len(mat[0])
		for row in mat:
			if len(row) != length:
				same_len = False
		if not same_len:
			raise MatrixError("The number of items in each row must be equal")
		self.__refresh_properties__(mat)

	def __refresh_properties__(self, mat):
		"""
		:param mat: A list representing the elements of the matrix to be refreshed. Each element is a row
		:return: None
		Called after any changes to a matrix to refresh its rows, columns, rank, etc.
		"""
		self.rows = [row for row in mat]
		col_lst = []
		for col_index in range(len(mat[0])):
			col_lst.append([row[col_index] for row in self.rows])
		self.cols = col_lst
		self.mat = mat
		self.rank = (len(self.rows), len(self.cols))

	@staticmethod
	def get_input():
		"""
		:return: A list used to construct a new Matrix object. Each element is a row
		Asks user for inputs through console rather than a hard coded input. Called if an empty matrix object is
		initialized.
		"""
		matrix_list = []
		try:
			rows = int(raw_input("Enter number of rows (m)... "))
			columns = int(raw_input("Enter number of columns (n)... "))
		except ValueError:
			raise MatrixError("Invalid dimensions")
		for m in range(0, rows):
			raw_row = raw_input("Row {0}: ".format(m + 1))
			parsed_row = raw_row.split(',') if ',' in raw_row else raw_row.split(' ')
			try:
				parsed_row = [int(x) for x in parsed_row]
			except ValueError:
				raise MatrixError("Invalid format for row")
			if len(parsed_row) != columns:
				raise MatrixError("Invalid row dimensions")
			matrix_list.append(parsed_row)
		return matrix_list

	def __repr__(self):  # problem if terms are more than one digit, columns not aligned
		matrix = self.mat
		string = ""
		for row in matrix:
			string += " ".join([str(x) for x in row]) + "\n"
		return string

	def add_row(self, new_row, i=None):
		"""
		:param new_row: The row to be insterted. Must be the same length as self.rank[1]
		:param i: The index to insert at. If none given, defaults to after last row
		:return: None
		Insert new_row (a list) at index i, defaulting to the end of the matrix.
		"""
		if len(new_row) != self.rank[1]:
			raise MatrixError("The new row must be the same length as the other rows")
		if i is None:
			i = self.rank[0]
		self.mat.insert(i, new_row)
		self.__refresh_properties__(self.mat)

	def add_col(self, new_col, i=None):
		"""
		:param new_col: The column to be inserted. Must be the same length as self.rank[0]
		:param i: The index to insert at. If none given, defaults to after last column
		:return: None
		Insert new_col (a list) at index i, defaulting to the end of the matrix.
		"""
		if len(new_col) != self.rank[0]:
			raise MatrixError("The new column must be the same length as the other columns")
		if i is None:
			i = self.rank[1]
		for row in self.mat:
			row.insert(i, new_col[0])
		self.__refresh_properties__(self.mat)

	def __add__(self, matrix_b):
		"""
		:param matrix_b: Matrix to add to self
		:return: Matrix object, sum of two matrices
		Add two matrices of equal rank element by element
		"""
		if type(matrix_b) != Matrix:
			raise MatrixError("Addition is only defined between two matrices of equal length")
		if self.rank != matrix_b.rank:
			raise MatrixError("The matrices must be of equal rank")
		new_matrix = Matrix(self.mat)
		for index, rowA in enumerate(new_matrix.rows):
			new_matrix.mat[index] = [sum(x) for x in zip(rowA, matrix_b.rows[index])]
		return Matrix(new_matrix.mat)

	def __mul__(self, left_term):
		"""
		:param left_term: The float, int, or Matrix to the left of self, to be multiplied on left of self
		:return: Matrix object (or in rare cases int or float) that results from matrix or scalar multiplication
		Multiplies left_term on left of matrix -- b * A multiplies each element in A by 2, B * A performs matrix
		multiplication with B left of A.
		"""
		print self.mat
		if type(left_term) != Matrix and type(left_term) != int and type(left_term) != float:
			raise MatrixError('Multiplication not defined for Matrix * {}'.format(type(left_term)))
		# if type(left_term) == int or type(left_term) == float:
		# work here
		'''else:
			if self.rank[0] != left_term.rank[1]:
				raise MatrixError, "Invalid dimensions"'''

	# def _rmul_(self, right_term):
	# def here for right multiplication
