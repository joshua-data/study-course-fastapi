from Enemy import *

zombie = Enemy()
zombie.type_of_enemy = 'Zombie'

msg = f"{zombie.type_of_enemy} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}"
print(msg)

zombie.talk()
zombie.walk_forward()
zombie.attack()
