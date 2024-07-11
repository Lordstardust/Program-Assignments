# ability.py
import random

class Ability:
    def __init__(self, name, max_damage):
        '''Initialize the attributes:
          name: String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and the max_damage.'''
        return random.randint(0, self.max_damage)

if __name__ == "__main__":
    ability = Ability("Super Punch", 50)
    print(ability.name)
    print(ability.attack())
