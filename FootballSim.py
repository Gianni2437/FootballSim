import Actions
import Calculations
import Objects

x = Objects.Team('Patriots', 10, 1)
y = Objects.Team('Falcons', 8, 7)

#coin flip for first possesion
teamWithPossesion = x
possessionCoinFlip = Calculations.coinToss(1)
if possessionCoinFlip < 0:
    teamWithPossesion = x
else: 
    teamWithPossesion = y
#Run one play, check for first down
Actions.play()
    
