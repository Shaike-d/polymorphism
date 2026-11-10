import classes_for_main_exe.class_Character as c


class Warrior(c.Character):

    def __init__(self,name,health):
        super().__init__(name,health)

    def attack_power(self):
        return 15
