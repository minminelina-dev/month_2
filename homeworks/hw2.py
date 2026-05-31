import random

class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Hi, I'm {self.name}, my level is {self.level}")

    def attack(self):
        print(f'{self.name} is attacking!!')
        self.strength -= 1

    def rest(self):
        print(f'{self.name} resting…')
        self.health += 1

class Warrior(Hero):

    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'{self.name} attacking with sword!')
        self.strength -= 1


class Mage(Hero):

    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f'{self.name} casting spell!')
        self.strength -= 1


class Assassin(Hero):

    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f'{self.name} sneak attacks!')
        self.strength -= 1

warrior  = Warrior( name='Jungkook', level=97, health=970, strength=97, stamina=85)
mage     = Mage(    name='Yoongi',   level=93, health=730, strength=93, mana=120)
assassin = Assassin(name='J-Hope',   level=94, health=940, strength=94, stealth=99)

heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()

wins_against = {
        'Warrior':  'Assassin',
        'Assassin': 'Mage',
        'Mage':     'Warrior',
    }

hero_map = {
        'Warrior':  warrior,
        'Mage':     mage,
        'Assassin': assassin,
    }
while True:
    print('-' * 40)
    print('Mini-game: rock, paper, scissors')

    print('Warrior  = Rock')
    print('Assassin = Scissors')
    print('Mage = Paper')

    user_choice = input('Choose your hero: Warrior / Mage / Assassin: ').strip().capitalize()

    while user_choice not in hero_map:
        print('Wrong choice! Try again.')
        user_choice = input('Choose your hero: Warrior / Mage / Assassin: ').strip().capitalize()

    opponents = list(hero_map.keys())
    opponents.remove(user_choice)
    computer_choice = random.choice(opponents)

    print(f'\nYou chose:  {user_choice}')
    print(f'Opponent chose:   {computer_choice}')
    print('-' * 40)

    hero_map[user_choice].attack()
    hero_map[computer_choice].attack()
    print('-' * 40)

    if wins_against[user_choice] == computer_choice:
        print(f'{user_choice} победил!')
    elif wins_against[computer_choice] == user_choice:
        print(f'{computer_choice} победил!')
    else:
        print('Draw!')

    play_again: str = input('\nPlay again? yes or no: ').strip().lower()

    if play_again != 'yes':
        print('Thanks for playing!')
        break