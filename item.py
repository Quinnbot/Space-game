"""
item modifacation
[strength, range]

player stats modifacation
[strength, agility, charisma]
"""


class item(object):

    def __init__(self, name, itemMod, playerMod):
        self.name = name
        self.itemMod = itemMod
        self.playerMod = playerMod

    def playerModifacation(self, choice):
        if(choice == 0):
            return self.playerMod[0]
        if(choice == 1):
            return self.playerMod[1]
        if(choice == 2):
            return self.playerMod[2]
        pass

    def itemModifacation(self, choice):
        if(choice == 0):
            return self.itemMod[0]
        if(choice == 1):
            return self.itemMod[1]
        pass

    def name(self):
        return self.name
