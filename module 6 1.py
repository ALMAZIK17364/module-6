#Родители
class Animal:
    alive = True
    fed = False

    def eat(self, food):
        if food.edible == True:
            print(self.name, " съел ", food.name)
            self.fed = True
        else:
            print(self.name, " не стал есть ", food.name)
            if self.fed == False:
                self.alive = False

class Plant:
    edible = False

#Наследники:
class Mammal(Animal):
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name):
        self.name = name
    pass

class Flower(Plant):
    def __init__(self, name):
        self.name = name
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name
    pass




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
