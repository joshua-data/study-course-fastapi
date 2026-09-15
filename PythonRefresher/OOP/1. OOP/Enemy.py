class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        msg = f"I am a {self.type_of_enemy}. Be prepared to fight!"
        print(msg)

    def walk_forward(self):
        msg = f"{self.type_of_enemy} moves closer to you"
        print(msg)

    def attack(self):
        msg = f"{self.type_of_enemy} attacks for {self.attack_damage} damage"
        print(msg)
