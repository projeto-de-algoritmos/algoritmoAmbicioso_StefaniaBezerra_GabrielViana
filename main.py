from knapsack import FractionalKnapSack

if __name__ == "__main__":
    bus = [1, 2, 3, 4]
    val = [2.50, 3.50, 5.00, 10.00]
    capacity = 50

    maxValue = FractionalKnapSack.getMaxValue(bus, val, capacity)
    print("Number of bus", bus)
    print("Number of value of pass", val)
    print("Maximum value in Knapsack =", maxValue)
