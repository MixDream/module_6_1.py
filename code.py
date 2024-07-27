class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")


class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


A1 = Predator('пьяный русский медведь')
A2 = Mammal('Кунг-фу панда')
P1 = Flower('цветик недоцветик')
P2 = Fruit('большой персик')

print(A1.name)
print(P1.name)
print(A1.alive)
print(A2.fed)
A1.eat(P1)
A2.eat(P2)
print(A1.alive)
print(A2.fed)
