import random
import Calculations

#Actions
def play(offense, defense):
    offensivePlay = Calculations.playOutcome(offense, defense)
    if offensivePlay is 'positive':
        yardsGained = random.randint(4,20)
        print("Nice Play: "+ str(yardsGained))
    elif offensivePlay is 'negative':
        yardsGained = random.randint(-10, 2)
        print("Bad Play: "+ str(yardsGained))
    else:
        yardsGained = random.randint(-3, 3)
        print("Stood up: "+ str(yardsGained))
    return yardsGained






