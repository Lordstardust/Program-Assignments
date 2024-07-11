# weapon.py
from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        '''Return a random value between half of the max_damage and the max_damage.'''
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)

if __name__ == "__main__":
    weapon = Weapon("Sword", 100)
    print(weapon.name)
    print(weapon.attack())
