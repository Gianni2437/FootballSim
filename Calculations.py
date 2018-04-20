import Actions
import random

#Based on team ratings decide the outcome of individual play in 3 categories: 
#positive, negative or meh (from the point of view of the offense)
def playOutcome(offense, defense):
    if offense.offensiveRating > defense.defensiveRating:
        totalCoinFlips = offense.offensiveRating - defense.defensiveRating
        outcome = coinToss(totalCoinFlips)
        if  outcome > 0:
            return 'positive'
        elif outcome <= -1:
            return 'negative'
        else:
            return 'meh'
    elif offense.offensiveRating < defense.defensiveRating:
        totalCoinFlips = defense.defensiveRating - offense.offensiveRating
        outcome = coinToss(totalCoinFlips)
        if  outcome > 0:
            return 'negative'
        elif outcome < 0:
            return 'postive'
        else:
            return 'meh'
    else:
        totalCoinFlips = 1
        outcome = coinToss(totalCoinFlips)
        if  outcome > 0:
            return 'negative'
        elif outcome < 0:
            return 'postive'
        else:
            return 'meh'

#Computes 50-50 coin toss, returns total number of 'heads' minus 'tails'
#For individual coint flips, -1 is tails and 1 is heads
def coinToss(number):
    recordList, heads, tails = [], 0, 0 # multiple assignment
    for i in range(number): # do this 'number' amount of times
         flip = random.randint(0, 1)
         if (flip == 0):
              #print("Heads")
              recordList.append("Heads")
              heads+=1
         else:
              #print("Tails")
              recordList.append("Tails")
              tails+=1
    #print(str(recordList))
    #print(heads-tails)
    return heads-tails
