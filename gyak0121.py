class Horse:
    def __init__(self, name , age , gender ):
        self.name = name
        self.age = age
        self.gender = gender
        self.isAlive = True
        self.children = []

    def die(self):
        self.isAlive = False

    def aging(self):
        self.age +=1

    def giving_birth(self, child):
        self.children.append(child)

class HospitalForHorses:
    def __init__(self):
        self.horses=[]

    def addHorse(self, HorseToAdd):
        self.horses.append(HorseToAdd)

    def addHorse(self, HorseToAdd):
        self.horses.index(number).isAlive = False