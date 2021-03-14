class Matrix:
    def __init__(self, rows):
        self.rows = rows

        # checks that the matrix is valid
        row_lengths = []
        rows_equal_check = 0
        for i in rows:
            row_lengths.append(len(i))
        for i in row_lengths:
            if i != row_lengths[0]:
                rows_equal_check += 1
        if rows_equal_check != 0:
            print('Error: Unequal row lengths!! ', 'Please re-enter this matrix\'s values')
            self.rows = None
            rows = [[0]]

        # defines the number of rows and columns
        self.numrows = len(rows)
        self.numcols = len(rows[0])
        self.dim = str(len(rows[0])) + '*' + str(len(rows))

    # defines elementary row operation methods
    def row_swap(self, x, y):
        self.rows[x], self.rows[y] = self.rows[y], self.rows[x]

    def row_scal_mult(self, x, y):
        temp_lst = []
        for i in self.rows[x]:
            temp_val = i * y
            temp_lst.append(temp_val)
        self.rows[x] = temp_lst

    def row_add(self, x, y, z=1.0):
        row_to_add = []
        for i in self.rows[y]:
            temp_val = i * z
            row_to_add.append(temp_val)
        summed_row = []
        for i in range(len(row_to_add)):
            summed_row.append(row_to_add[i] + self.rows[x][i])
        self.rows[x] = summed_row

    # method for selecting a sub-matrix
    def sub_mat(self, col=None, row=None):
        mat_to_return = self.rows
        if col != None:
            for i in range(len(mat_to_return)):
                mat_to_return[i].pop(int(col))
        if row != None:
            mat_to_return.pop(row)
        return mat_to_return

    # defines matrix addition
    def __add__(self, other):
        if self.numrows == other.numrows and self.numcols == other.numcols:
            matrix_sum = []
            for i in range(self.numrows):
                new_row = []
                lst_of_tups = list(zip(self.rows[i], other.rows[i]))
                for j in lst_of_tups:
                    sum_ = j[0] + j[1]
                    new_row.append(sum_)
                matrix_sum.append(new_row)
            return matrix_sum
        else:
            print('Error: unequal matrices!!')

    # defines matrix multiplication
    def __mul__(self, other):
        if self.numrows == other.numcols:
            mat_mult = []
            for i in range(len(self.rows)):
                row_i = self.rows[i]
                col_j = []
                for j in range(other.numcols):


    # creates the row echelon form method
    def echelon (self):
        for j in range(len(self.rows)):
            # identify the pivot row
            for i in range(j, len(self.rows)):
                if self.rows[i][j] == 0:
                    pass
                else:
                    self.row_swap(j,i)
                    break
            # create the pivot
            if self.rows[j][j] != 0:
                self.row_scal_mult(j, 1/self.rows[j][j])
            # creates zeros below the pivot
            if j != len(self.rows)-1:
                for i in range(j+1, len(self.rows)):
                    self.row_add(i, j, -1*self.rows[i][j])






#tests
test_matrix = Matrix([[1,0,0],[0,1,0], [0,0,1]])
test_matrix.echelon()
print(test_matrix.rows)