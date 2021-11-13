from abc import abstractmethod, ABC
import math


class Laptop:
    def __init__(self, name: str, cpu_cores: int, core_power: float):
        """
        Constructor fo Laptop class Inits class properties
        :param name: The Laptop brand name
        :param cpu_cores: Number of cpu cores
        :param core_power: Each CPU power in GHz
        """
        self.name = name
        self.cpu_cores = cpu_cores
        self.core_power = core_power

    def total_cpu_power(self):
        """
        Calculate total CPU power by multiplication of core number and of CPUs
        :return: float: Total CPU power
        """
        self.__log("Total CPU power")
        return self.cpu_cores * self.core_power

    def __log(self, value):
        print(value)


class Abonent:
    def __init__(self, name: str, surname: str, patronymic: str, birth: str, male: str, date: str,
                 balance: float, tarif: str):
        """

        :param name: The name of Abonent
        :param surname: Surname of Abonent
        :param patronymic: Patronymic of Abonent
        :param birth: Birthday
        :param male: Gender
        :param date: Date of connection to tarif
        :param balance: Current balance pocket of Abonent
        :param tarif: Name of tarif
        """
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth = birth
        self.male = male
        self.date = date
        self.balance = balance
        self.tarif = tarif


class Transport(ABC):

    def __init__(self, ram_weight: float, wheel_weight: float):
        self.ram_weight = ram_weight
        self.wheel_weight = wheel_weight

    @abstractmethod
    def calculate_weight(self):
        pass


class Bicycle(Transport):
    number_of_wheels = 2

    def calculate_weight(self):
        return self.ram_weight + Bicycle.number_of_wheels * self.wheel_weight


class MotoTransport(Transport, ABC):

    def __init__(self, ram_weight: float, wheel_weight: float, engine_weight: float):
        super().__init__(ram_weight, wheel_weight)
        self.engine_weight = engine_weight


class MotoBike(MotoTransport):
    number_of_wheels = 2

    def calculate_weight(self):
        return self.ram_weight + Bicycle.number_of_wheels * self.wheel_weight + self.engine_weight


class Abonent:
    def __init__(self, name: str, surname: str, patronymic: str, birth: str,
                 male: str, connection_data: str, balance: float, tarif: str):
        '''

        :param name: the name of Abonent
        :param surname:  surname of Abonent
        :param patronymic:  patronomic of Abonent
        :param birth: Abonents btirth day
        :param male: male or female
        :param connection_data: data of connection
        :param balance: Abonent's balance
        :param tarif: the name of tarif
        '''
        self.name = name
        self.surname = surname
        self.patronomic = patronymic
        self.birth = birth
        self.male = male
        self.connection_data = connection_data
        self.balance = balance
        self.tarif = tarif


class Figura(ABC):

    @abstractmethod
    def calculate_square(self):
        pass

    @abstractmethod
    def calculate_perimetr(self):
        pass


class Circle(Figura):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def calculate_square(self):
        return math.pi * self.radius * self.radius

    def calculate_perimetr(self):
        return math.pi * self.radius * 2


class Quadrangle(Figura, ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b


class Rectangle(Quadrangle):
    def __init__(self, a: float, b: float):
        super().__init__(a, b)

    def calculate_perimetr(self):
        return 2 * (self.a + self.b)

    def calculate_square(self):
        return self.a * self.b


class Parallelogram(Quadrangle):
    def __init__(self, a: float, b: float, angle: float):
        super().__init__(a, b)
        self.angle = angle

    def calculate_perimetr(self):
        return 2 * (self.a + self.b)

    def calculate_square(self):
        return math.sin(math.radians(self.angle)) * self.b * self.a


class Trapezoid(Quadrangle):
    def __init__(self, a: float, b: float, c: float, d: float, angle1: float, angle2: float, h: float):
        '''

        :param a: bottom base
        :param b: top base
        :param c: left edge
        :param d: right edge
        :param angle1: angle between base and left edge
        :param angle2: angle between base and right edge
        :param h: trapezoid height
        '''
        super().__init__(a, b)
        self.angle1 = angle1
        self.angle2 = angle2
        self.c = c
        self.d = d
        self.h = h

    def calculate_square(self):
        return ((self.a + self.b) / 2) * self.h

    def calculate_perimetr(self):
        return self.a + self.b + self.c + self.d


class Writer:
    def __init__(self, birth: str, death, name:str, surname: str, alias: str, country: str):
        self.birth = birth
        self.death = death
        self.name = name
        self.surname = surname
        self.alias = alias
        self.country = country
        self.works = []

    def add_work(self, work):
        self.works.append(work)
        work.authors.append(self)

class Work(ABC):
    def __init__(self, authors: list, publisher: list, year: str):
        self.authors = authors
        self.publisher = publisher
        self.year = year

    def add_author(self, author: Writer):
        self.authors.append(author)
        author.works.append(self)

class Book(Work):
    def __init__(self, authors: list, publisher: list, year: str, binding: str, cover: str):
        super().__init__(authors, publisher, year)
        self.binding = binding
        self.cover = cover

class Journal(Work):
    def __init__(self, authors: list, publisher: list, year: str, covertype: str):
        super().__init__(authors, publisher, year)
        self.covertype = covertype

class Publication(Work):
    def __init__(self, authors: list, publisher: list, year: str,publication: str):
        super().__init__(authors, publisher, year)
        self.publication = publication

class Publisher:
    def __init__(self, name: str, foundation: str):
        '''

        :param name: the title of the publication
        :param foundation: year of foundation
        '''
        self.name = name
        self.foundation = foundation
        self.works = []

    def add_work(self, work):
        self.works.append(work)
        work.publisher.append(self)
#
# book = Book(['Abobus', 'Avtobus'], ['a', 'b'], '2005', 'hard', 'nice')
# writer = Writer('15.01.1999', None, 'Markus', 'Aboba', '','Ukraine')
# book.add_author(writer)
# print(book.authors)
# print(writer.works)