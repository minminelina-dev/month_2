from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name: str, level: int, health: int, strength: int):
        self.name     = name
        self.level    = level
        self.__health = health
        self.strength = strength

    def get_health(self) -> int:
        return self.__health

    def greet(self):
        print(f"Hi, I'm {self.name}, my level is {self.level}")

    def rest(self):
        print(f"{self.name} is resting")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Warrior is attacking with sword!")


class Mage(Hero):
    def attack(self):
        print("Mage is casting spell!")


class Assassin(Hero):
    def attack(self):
        print("Assassin sneak attacks!")

if __name__ == "__main__":
    warrior  = Warrior ("Oscar Piastri",   level=10, health=150, strength=80)
    mage     = Mage    ("Lando Norris", level=15, health=90,  strength=60)
    assassin = Assassin("Alex Albon",    level=12, health=110, strength=70)

    heroes = [warrior, mage, assassin]

    for hero in heroes:
        print("-" * 35)
        hero.greet()
        hero.attack()
        print(f"  HP before rest : {hero.get_health()}")
        hero.rest()
        print(f"  HP after rest     : {hero.get_health()}")
