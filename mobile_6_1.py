# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


# Дочерний класс Mammal от Animal
class Mammal(Animal):
    pass


# Дочерний класс Predator от Animal
class Predator(Animal):
    pass


# Дочерний класс Flower от Plant
class Flower(Plant):
    pass


# Дочерний класс Fruit от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем атрибут съедобности


# Создание объектов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка имен
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверка состояния животных
print(a1.alive)  # True
print(a2.fed)    # False

# Кормление
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин

# Повторная проверка состояния животных
print(a1.alive)  # False
print(a2.fed)    # True

