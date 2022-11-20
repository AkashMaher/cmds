class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def sortingKey(item: Item):
    return item.value / item.weight

def fractionalKnapsack(items, weightLimit):
    finalvalue = 0.0
    items.sort(key=sortingKey, reverse=True)

    for item in items:
        if item.weight < weightLimit: 
            weightLimit -= item.weight
            finalvalue += item.value
        else: # overflow
            finalvalue += item.value * (weightLimit / item.weight)
            break
    return finalvalue

w = 50
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
res = fractionalKnapsack(items,w)
print(res)
