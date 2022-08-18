import random
import itertools

def totalResults(headsTotal,tailsTotal):
    print('The total number of heads is: %s' % headsTotal)
    print('The total number of tails is: %s' % tailsTotal)

def streaks(results):
    bestHeads = max(sum(1 for _ in l) for n, l in itertools.groupby(results))
    bestTails = max(sum(1 for _ in l) for n, l in itertools.groupby(results))
    print("Longest heads streak:%s" %bestHeads)
    print("Longest tails streak:%s" %bestTails)

def numOfFlips():
    flipsNum = int(input("How many coin flips would you like to do?"))
    headsTotal = 0
    tailsTotal = 0
    results = []
    for i in range(flipsNum):
        HOrT = random.choice(["heads","tails"])
        print("Result %s is: %s" %(i+1,HOrT))
        if HOrT == "heads":
            headsTotal = headsTotal + 1
            results.append(1)
        else:
            tailsTotal = tailsTotal + 1 
            results.append(0)
    totalResults(headsTotal,tailsTotal)
    streaks(results)

numOfFlips()
