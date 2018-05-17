from item import item

class inventory(object):

    def __init__(self):

        itemModifacation = [0,0]
        playerModifacation = [0,0,0]
        self.items = [item("placeholder pants", itemModifacation, playerModifacation)]

        pass

    def addItem(self, name, itemMod, playerMod):
        newitem = item(name, itemMod, playerMod)
        self.items.append(newitem)
        pass

    def removeItem(self,name):
        for x in range(0, len(self.items)):
            if(self.items[x].name == name):
                del self.items[x]
        pass

    def listItems(self):
        for x in range(0, len(self.items)):
            print(x,":",self.items[x].name)
        pass

    def itemStats(self, name, choice):
        for x in range(0, len(self.items)):
            if(self.items[x].name == name):
                return self.items[x].itemModifacation(choice)

    def playerModStats(self, name, choice):
        for x in range(0, len(self.items)):
            if(self.items[x].name == name):
                return self.items[x].playerModifacation(choice)
