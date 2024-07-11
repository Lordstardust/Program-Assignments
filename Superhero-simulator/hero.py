# hero.py
class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def battle(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''
        winner = random.choice([self.name, opponent.name])
        return f'The randomly selected winner is {winner}'

if __name__ == "__main__":
    hero1 = Hero("Grace Hopper", 200)
    hero2 = Hero("Alan Turing", 200)
    print(hero1.battle(hero2))
# hero.py
from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = sum([ability.attack() for ability in self.abilities])
        return total_damage

    def defend(self):
        total_block = sum([armor.block() for armor in self.armors])
        return total_block

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def battle(self, opponent):
        while self.current_health > 0 and opponent.current_health > 0:
            opponent.take_damage(self.attack())
            if opponent.current_health <= 0:
                return f'{self.name} won!'
            self.take_damage(opponent.attack())
            if self.current_health <= 0:
                return f'{opponent.name} won!'
        return 'Draw'

if __name__ == "__main__":
    hero1 = Hero("Grace Hopper", 200)
    hero2 = Hero("Alan Turing", 200)

    ability1 = Ability("Super Punch", 50)
    armor1 = Armor("Shield", 30)
    hero1.add_ability(ability1)
    hero1.add_armor(armor1)

    ability2 = Ability("Coding Skills", 40)
    armor2 = Armor("Firewall", 25)
    hero2.add_ability(ability2)
    hero2.add_armor(armor2)

    print(hero1.battle(hero2))
# hero.py
from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = sum([ability.attack() for ability in self.abilities])
        return total_damage

    def defend(self):
        total_block = sum([armor.block() for armor in self.armors])
        return total_block

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def battle(self, opponent):
        while self.current_health > 0 and opponent.current_health > 0:
            opponent.take_damage(self.attack())
            if opponent.current_health <= 0:
                return f'{self.name} won!'
            self.take_damage(opponent.attack())
            if self.current_health <= 0:
                return f'{opponent.name} won!'
        return 'Draw'

if __name__ == "__main__":
    hero1 = Hero("Grace Hopper", 200)
    hero2 = Hero("Alan Turing", 200)

    ability1 = Ability("Super Punch", 50)
    armor1 = Armor("Shield", 30)
    weapon1 = Weapon("Sword", 100)
    hero1.add_ability(ability1)
    hero1.add_armor(armor1)
    hero1.add_weapon(weapon1)

    ability2 = Ability("Coding Skills", 40)
    armor2 = Armor("Firewall", 25)
    hero2.add_ability(ability2)
    hero2.add_armor(armor2)

    print(hero1.battle(hero2))
