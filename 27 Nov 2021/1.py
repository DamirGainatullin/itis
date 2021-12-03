class Sudoku():

    def __init__(self):
        self.s = [[0 for _ in range(0, 9)] for _ in range(0, 9)]

    def add(self, x, y, value):
        self.s[x][y] = value

    def check_full(self):
        for x in range(0, 9):
            for y in range(0, 9):
                if self.s[x][y] != 0:
                    return False
        return True

    def check_value(self):
        for x in range(0, 9):
            for y in range(0, 9):
                if 0 >= self.s[x][y] or self.s[x][y] >= 9:
                    return False
        return True

    def check_of_lines(self):
        for i in range(0, 9):
            a = self.s[i]
            a.sort()
            if a != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        return True

    def check_line_incomplete(self):
        for i in range(0, 9):
            a = (self.s[i])
            if len(a) - len(set(a)) != a.count(0) - 1:
                return False
        return True

    def check_of_column(self):
        for x in range(0, 9):
            col = []
            for y in range(0, 9):
                col.append(self.s[y][x])
            col.sort()
            if col != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        return True

    def check_column_incomplete(self):
        for x in range(0, 9):
            col = []
            for y in range(0, 9):
                col.append(self.s[y][x])
            if len(col) - len(set(col)) != col.count(0) - 1:
                return False
        return True

    def check_square(self):
        for x in range(0, 7, 3):
            for j in range(0, 7, 3):
                square = []
                for x in range(3):
                    for y in range(3):
                        square.append(self.s[x + x][j + y])
                if square != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
        return True

    def check_square_incomplete(self):
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                square = []
                for x in range(3):
                    for y in range(3):
                        square.append(self.s[i + x][j + y])
                if len(square) - len(set(square)) != square.count(0) - 1:
                    return False
        return True
