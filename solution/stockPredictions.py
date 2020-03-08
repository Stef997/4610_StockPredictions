import numpy

def printTransactions(m, k, d, name, owned, prices):

    spikeH = None
    spikeL = None

    for i in range(k):
        currentSpike = getSpike(prices[i])

        if currentSpike > 0 and owned[i] > 0 and (spikeH is None or currentSpike > spikeH[0]):
            spikeH = (currentSpike, '{0} SELL {1}'.format(name[i], owned[i]))

        elif currentSpike > 0 and d > 0 and m > prices[i][-1] and (spikeL is None or currentSpike < spikeL[0]):
            spikeL = (currentSpike, '{0} BUY {1}'.format(name[i], int(m / prices[i][-1])))

    if spikeH != None and spikeL != None:
        print(2)
    elif spikeH != None or spikeL != None:
        print(1)
    else:
        print(0)

    if spikeH != None:
        print(spikeH[1])
    if spikeL != None:
        print(spikeL[1])


def getSpike(n):
    total = 0
    for i in n:
        total += i
    avg = numpy.mean(n)
    avg -= avg / len(n)
    avg += n[len(n)-1] / len(n) * (1.5)
    
    return avg - numpy.mean(n)

def start():
    line = input().split()
    m, k, d = float(line[0]), int(line[1]), int(line[2])
    name = []
    owned = []
    prices = []

    for i in range(k):
        line = input().split()
        name.append(line[0])
        owned.append(int(line[1]))
        prices.append(list(map(float, line[2:])))        
    printTransactions(m, k, d, name, owned, prices)

start()
