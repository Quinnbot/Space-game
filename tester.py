#tester
from entity import entity


# from inventory import inventory


stat = [10, 10, 10, 1000]


itemModifacation = [2,1]
playerModifacation = [1,1,1]

pla = entity("Quinny", stat)
pla.addItem("water", itemModifacation, playerModifacation)
pla.listItems()
print("\n\n")
pla.listItems()

print(pla.itemStats("water", 0))
print(pla.stats(3))
print(pla.name)
