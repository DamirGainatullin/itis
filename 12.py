import math


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, a):
        return Vector2D(self.x + a.x, self.y + a.y)

    def add2(self, a):
        self.x += a.x
        self.y += a.y

    def sub(self, a):
        return Vector2D(self.x - a.x, self.y - a.y)

    def sub2(self, a):
        self.x -= a.x
        self.y -= a.y

    def mult(self, a):
        return Vector2D(self.x * a, self.y * a)

    def mult2(self, a):
        self.x *= a
        self.y *= a

    def __str__(self):
        return "%s/%s" % (self.x, self.y)

    def len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cos(self, a):
        return (self.x * a.x + self.y + a.y) / (self.len() * a.len())

    def scalarProduct(self, a):
        return self.len() * a.len() * self.cos(a)

    def equals(self, a):
        if self.len() < a.len():
            return '<'
        elif self.len() > a.len():
            return '>'
        else:
            return '='

class RationalFraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reduce(self):
        maxx = 1
        minn = min(self.a, self.b)
        for i in range(1, minn):
            if self.a % i == 0 and self.b % i == 0:
                if self.a % (minn // i) == 0 and self.b % (minn // i) == 0:
                    if (minn // i) > maxx:
                        maxx = minn // i
                else:
                    if i > maxx:
                        maxx = i
        self.a //= maxx
        self.b //= maxx

    def add(self, a):
        general = self.b * a.b
        res1 = self.a * a.b + a.a * self.b
        res = RationalFraction(res1, general)
        res.reduce()
        return res

    def add2(self,a):
        general = self.b * a.b
        self.a = self.a * a.b + a.a * self.b
        self.b = general
        self.reduce()

    def sub(self, a):
        general = self.b * a.b
        res1 = self.a * a.b - a.a * self.b
        res = RationalFraction(res1, general)
        res.reduce()
        return res

    def sub2(self,a):
        general = self.b * a.b
        self.a = self.a * a.b - a.a * self.b
        self.b = general
        self.reduce()

    def mult(self, a):
        res = RationalFraction(self.a * a.a, self.b * a.b)
        res.reduce()
        return res

    def mult2(self, a):
        self.a *= a.a
        self.b *= a.b
        self.reduce()

    def div(self, a):
        if a.value() == 0:
            return 'Error'
        res = RationalFraction(self.a * a.b, self.b * a.a)
        res.reduce()
        return res

    def div2(self, a):
        if a.value() == 0:
            return 'Error'
        self.a *= a.b
        self.b *= a.a
        self.reduce()

    def __str__(self):
        return f'{self.a}/{self.b}'

    def value(self):
        return self.a / self.b

    def equals(self, a):
        if self.value() < a.value():
            return '<'
        elif self.value() > a.value():
            return '>'
        else:
            return '='
    def numberPart(self):
        return int(self.value())

class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self, a):
        return ComplexNumber(self.a + a.a, self.b + a.b)

    def add2(self, a):
        self.a += a.a
        self.b += a.b

    def sub(self, a):
        return ComplexNumber(self.a - a.a, self.b - a.b)

    def sub2(self, a):
        self.a -= a.a
        self.b -= a.b

    def multNumber(self,x):
        return ComplexNumber(self.a * x, self.b * x)

    def multNumber2(self, x):
        self.a *= x
        self.b *= x

    def mult(self, a):
        return ComplexNumber(self.a * a.a - self.b * a.b, self.a * a.b + self.b * a.a)

    def mult2(self, a):
        self.a = self.a * a.a - self.b * a.b
        self.b = self.a * a.b + self.b * a.a

    def div(self, a):
        if a.a == 0 and a.b == 0:
            return 'Error'
        return ComplexNumber((self.a * a.a + self.b * a.b)/(a.a * a.a + a.b + a.b),
                             (self.b * a.a - self.a * a.b)/(a.a * a.a + a.b + a.b))


    def div2(self, a):
        if a.a == 0 and a.b == 0:
            return 'Error'
        self.a = (self.a * a.a + self.b * a.b)/(a.a * a.a + a.b + a.b)
        self.b = (self.b * a.a - self.a * a.b)/(a.a * a.a + a.b + a.b)

    def len(self):
        return (self.a * self.a + self.b * self.b) ** 0.5

    def __str__(self):
        if self.b < 0:
            return f'{self.a} - {self.b}*i'
        else:
            return f'{self.a} + {self.b}*i'

    def arg(self):
        return math.atan2(self.b, self.a)

    def pow(self, x):
        return math.pow(self.len(),x) * (math.cos(x * self.arg()) + math.sin(x * self.arg))

    def equals(self, a):
        if self.a == a.a and self.b == a.b:
            return '='
        else:
            return '!='

class Matrix2x2:
    def __init__(self, a=None):
        if a is None:
            a = [[0, 0], [0, 0]]
        self.a = a
    def set(self, i, j, x):
        self.a[i][j] = x

    def add(self, a):
        return Matrix2x2([[self.a[0][i] + a.a[0][i] for i in [0, 1]],
                          [self.a[1][i] + a.a[1][i] for i in [0, 1]]])

    def add2(self, a):
        self.a = [[self.a[0][i] + a.a[0][i] for i in [0, 1]],
         [self.a[1][i] + a.a[1][i] for i in [0, 1]]]

    def sub(self, a):
        return Matrix2x2([[self.a[0][i] - a.a[0][i] for i in [0, 1]],
                          [self.a[1][i] - a.a[1][i] for i in [0, 1]]])

    def sub2(self, a):
        self.a = [[self.a[0][i] - a.a[0][i] for i in [0, 1]],
                  [self.a[1][i] - a.a[1][i] for i in [0, 1]]]

    def multNumber(self, x):
        return Matrix2x2(list(map(lambda z: z * x, self.a)))

    def multNumber2(self, x: float):
        for i in range(2):
            for j in range(2):
                self.a[i][j] *= x


    def mult(self, a):
        res = []
        for i in range(2):
            res.append([self.a[i][0] * a.a[0][0] + self.a[i][1] * a.a[1][0],
                        self.a[i][0] * a.a[0][1] + self.a[i][1] * a.a[1][1]])
        return Matrix2x2(res)

    def mult2(self, a):
        for i in range(2):
            self.a[i] = [self.a[i][0] * a.a[0][0] + self.a[i][1] * a.a[1][0],
                        self.a[i][0] * a.a[0][1] + self.a[i][1] * a.a[1][1]]

    def det(self):
        return self.a[0][0] * self.a[1][1] - self.a[0][1] * self.a[1][0]


    def transpon(self):
        self.a[0][1], self.a[1][0] = self.a[1][0], self.a[0][1]

    def inverseMatrix(self):
        self.a[0][0], self.a[1][1], self.a[0][1], self.a[1][0] = \
            self.a[1][1], self.a[0][0], -self.a[1][0], -self.a[0][1] #matrix of minors
        self.transpon()
        return Matrix2x2(self.multNumber2(1/self.det()))

    def equivalentDiagonal(self):
        pass

    def multVector(self, b):
        return Vector2D(self.a[0][0] * b.x + self.a[0][1] * b.y,
                        self.a[1][0] * b.x + self.a[1][1] * b.y)
    
a = Matrix2x2([[1, 2],[3, 4]])
b = Matrix2x2([[5, 6],[7, 8]])
a.inverseMatrix()
print(a.a)