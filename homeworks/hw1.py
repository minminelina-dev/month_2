print('"Dream, even if it breaks your heart." — BTS, Young Forever')
print('Every hero starts with a dream. This is where theirs begins...\n')

class Hero:

    # class constructor
    def __init__(self, name, level, health, strength):
        # class attributes
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # class methods
    def greet(self):
        print(f"Hi, I'm {self.name}, my level is {self.level}")

    def attack(self):
        print(f'{self.name} is attacking!!')
        self.strength -= 1

    def rest(self):
        print(f'{self.name} resting…')
        self.health += 1

jungkook = Hero('Jungkook', 97, 970, 97)  # born in 1997

yoongi = Hero('Yoongi', 93, 730, 93)  # born in 1993, 730 = mix of his fav number 7 and 3 (BTS)

jhope = Hero('J-Hope', 94, 940, 94)  # born in 1994

heroes = [jungkook, yoongi, jhope]

for hero in heroes:
    print(f'\n{"=" * 30}')
    hero.greet()

    print(f'Strength before attack: {hero.strength}')
    hero.attack()
    print(f'Strength after attack: {hero.strength}')

    print(f'Health before rest: {hero.health}')
    hero.rest()
    print(f'Health after rest: {hero.health}')

print('\nThey fought, got hurt, rested, and kept going.')
print('"Dream, even if it breaks your heart." — BTS, Young Forever')