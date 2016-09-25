class MatrixError(Exception):
    pass


class Matrix(object):
    def __init__(self, mat=None):
        if mat is None:
            mat = get_input()
        length = len(mat[0])
        for row in mat:
            for element in row:
                if not isinstance(element, (int, long, float, complex)):
                    raise MatrixError("All elements must be numbers")
            if len(row) != length:
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

    def __repr__(self):  # problem if terms are more than one digit, columns not aligned
        matrix = self.mat
        string = ""
        for row in matrix:
            string += " ".join([str(x) for x in row]) + "\n"
        return string

    def add_row(self, new_row, i=None):
        """
        :param new_row: The row to be inserted. Must be the same length as self.rank[1]
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

    def __neg__(self):
        """
        :return: Matrix object with each term multiplied by -1
         Get -1 * self
        """
        return -1 * self

    def __add__(self, matrix_b):
        """
        :param matrix_b: Matrix to add to self
        :return: Matrix object, sum of two matrices
        Add two matrices of equal rank element by element
        """
        if not isinstance(matrix_b, Matrix):
            raise MatrixError("Addition is only defined between two matrices of equal length")
        if self.rank != matrix_b.rank:
            raise MatrixError("The matrices must be of equal rank")
        new_mat = []
        for index, rowA in enumerate(self.rows):
            new_mat.append([sum(x) for x in zip(rowA, matrix_b.rows[index])])
        return Matrix(new_mat)

    def __sub__(self, matrix_b):
        """
        :param matrix_b: Matrix to add to self
        :return: Matrix object, sum of two matrices
        Add two matrices of equal rank element by element
        """
        if not isinstance(matrix_b, Matrix):
            raise MatrixError("Subtraction is only defined between two matrices of equal length")
        if self.rank != matrix_b.rank:
            raise MatrixError("The matrices must be of equal rank")
        return self + (-matrix_b)

    def __rmul__(self, left_term):
        """
        :param left_term: The float, int, long, or complex number to the left of self, to be multiplied on left of self
        :return: Matrix object that results from scalar multiplication
        Multiplies left_term on left of matrix -- b * A multiplies each element in A by b
        """
        if not isinstance(left_term, (int, long, float, complex)):
            raise MatrixError('Multiplication not defined for Matrix * {}'.format(type(left_term)))
        new_mat = [[element * left_term for element in row] for row in self.rows]
        return Matrix(new_mat)

    def __mul__(self, right_term):
        """
        :param right_term: The Matrix object to the right of self, to be multiplied on right of self
        :return: Matrix object that results from matrix multiplication
        Multiplies two matrices, with self on left -- A * B performs matrix multiplication of A and B
        """
        if not isinstance(right_term, Matrix):
            raise MatrixError('Multiplication not defined for Matrix * {}'.format(type(right_term)))
        new_mat = [[0 for element in range(self.rank[1])] for row in range(right_term.rank[0])]
        for i in range(self.rank[0]):
            for j in range(right_term.rank[1]):
                for k in range(right_term.rank[0]):
                    new_mat[i][j] += self.mat[i][k] * right_term.mat[k][j]
        return Matrix(new_mat)

    def __pow__(self, n):
        """
        :param n: The power to raise self to
        :return: Matrix object resulting from raising self to the nth power
        Raise self to the nth power -- A ** n returns A^n
        """
        new_mat = Matrix(self.mat)
        for i in range(n-1):
            new_mat = new_mat * self
        return new_mat


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
