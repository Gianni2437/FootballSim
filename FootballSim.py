import Actions
import Calculations
import Objects

Pats = Objects.Team('Patriots', 10, 1)
Falc = Objects.Team('Falcons', 8, 7)
for x in range (0,4):
    Actions.play(Pats, Falc)
