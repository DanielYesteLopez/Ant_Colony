'''
Definir clase hormiga:
Contiene
·Asset
·Comportamiento
·Características
·
'''

import random

class Ant:
    sprite = ""
    positionX = 0
    positionY = 0
    def __init__(self, sprite,position):
        self.asset = sprite
        self.positionX = 0
        self.positionY = 0



    def possibleExpansions(self):
        #Posición sera un par x,y
        nextPositionX = random.randint(self.positionX,self.positionX+1)
        nextPositionY = random.randint(self.positionX,self.positionY+1)
        return nextPositionX,nextPositionY