import FootballSim
#Objects and Instances

#Team class with name, offesnive and defensive rating
class Team:
    def __init__(self, name, offensiveRating, defensiveRating):
        self.name = name
        self.offensiveRating = offensiveRating
        self.defensiveRating = defensiveRating
        
class Field:
    totalYards = 120

    def __init__(self, currentPos, firstDownPos, scrimmage):
        self.currentPos = currentPos
        self.firstDownPos = firstDownPos
        self.scrimmage = scrimmage
    def moveTheChains(self, currentPos, firstDownPos):
        if (self.currentPos + 10 < 110):
            self.firstDownPos = self.currentPos + 10
        else:
            self.firstDownPos = 121
    






