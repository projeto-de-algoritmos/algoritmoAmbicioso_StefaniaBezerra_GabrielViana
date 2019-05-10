class BusValue:
    def __init__(self, bus, val, index):
        self.bus = bus
        self.val = val
        self.index = index
        self.cost = val // bus

    def __lt__(self, other):
        return self.cost < other.cost

class FractionalKnapSack:

    @staticmethod
    def getMaxValue(bus, val, capacity):

        indexVal = []
        for counter in range(len(bus)):
            indexVal.append(BusValue(bus[counter], val[counter], counter))

        indexVal.sort(reverse = True)

        totalValue = 0
        for counter in indexVal:
            currentBus = int(counter.bus)
            currentVal = int(counter.val)
            if capacity - currentBus >= 0:
                capacity -= currentBus
                totalValue += currentVal
            else:
                fraction = capacity / currentBus
                totalValue += currentVal * fraction
                capacity = int(capacity - (currentBus * fraction))
                break
        return totalValue
