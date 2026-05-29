# 2: принципы ООП -  Наследование, Полиморфизм.
# Гит - коммиты, создание репозитория, git push

# Наследование
# родительский класс!!
class Hero:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.health = hp

    def action(self):
        return f"{self.name} base action!!"

# дочерний класс или сабкласс
class MageHero(Hero):

    def __init__(self, name, level, hp, mp):
        super().__init__(name, level, hp)
        self.mp = mp

    def action(self):
        return f"this new action {self.name}"

    def cast_spell(self):
        return f"{self.name} Fire!!"
kirito = Hero('Kirito', 10, 10)
gendalf_silver = MageHero('Gendalf', 20, -20, 100)

# print(kirito.action())
# print(gendalf_silver.action())

# виды наследования (вертикальное, горизонтальное и ромбовидное)
class Fly:
    def f_action(self):
        return "Fly!!"

class Swim:
    def s_action(self):
        return "Swim!!"

class Animal(Swim, Fly):
    def action(self):
        return "action"

donald_duck = Animal()

# print(donald_duck.action())
# print(donald_duck.f_action())
# print(donald_duck.s_action())

class A:
    def action(self):
        print('A')

class B(A):
    def action(self):
        super().action()
        print('B')

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B, C):
    def action(self):
        super().action()
        return 'D'

test_obj = D()
print(test_obj.action())
print(D.mro())

