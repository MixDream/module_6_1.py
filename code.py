class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True
a1 = Predator('пьяный русский медведь')
a2 = Mammal('Кунг-фу панда')
p1 = Flower('Цветик недоцветик')
p2 = Fruit('большой персик')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
