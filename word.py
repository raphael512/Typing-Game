import random

class word:
    word = ""
    active = False
    y = 0
    x = 0
    count = 0

    def __init__(self, word):
        self.word = word
        self.active = False
        self.x = random.randint(50, 600)

    def setActive(self, act):
        self.active = act 

    def getActive(self):
        return self.active 

    def setWord(self, word):
        self.word = word 

    def getWord(self):
        return self.word 

    def setY(self, num):
        self.y = num
    
    def getY(self):
        return self.y

    def setX(self, num):
        self.x = num

    def getX(self):
        return self.x

    def setCount(self, num):
        self.count = num

    def getCount(self):
        return self.count
