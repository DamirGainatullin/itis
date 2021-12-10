class Abiturient:
    def __init__(self, score: int, name: str, surname: str, objects: list):
        '''

        :param score: sum of all balls
        :param name: name
        :param surname: surname
        :param objects: list of objects EGE
        '''
        self.score = score
        self.name = name
        self.surname = surname
        self.objects = objects


class Fakultet:
    def __init__(self, name: str, score: int, objects: list, score_blatnie: int):
        '''

        :param name: name
        :param score: minimum sum of balls for admission
        :param objects: list of objects EGE
        :param score_blatnie: minimum sum of balls for free admission
        '''
        self.name = name
        self.score = score
        self.objects = objects
        self.score_blatnie = score_blatnie
        self.platnie = []
        self.blatnie = []
        self.abiturients = []

    def add_abiturient(self, abiturient: Abiturient):
        self.abiturients.append(abiturient)
        if self.objects <= abiturient.objects and abiturient.score >= self.score:
            if abiturient.score >= self.score_blatnie:
                self.blatnie.append(abiturient)
            else:
                self.platnie.append(abiturient)

    def abiturients_check(self):
        self.blatnie = sorted(self.blatnie)
        self.platnie = sorted(self.platnie)
        print('Платники')
        for i in range(len(self.blatnie)):
            print(i + 1, self.blatnie[i].name, self.blatnie[i].surname, self.blatnie[i].score)
        print('Бюджетники')
        for i in range(len(self.platnie)):
            print(i + 1, self.platnie[i].name, self.platnie[i].surname, self.platnie[i].score)


class Vuz:
    def __init__(self):
        self.fakultets = []
