import random
class Point:
    x, y, label = 0.0 , 0.0 , 0
    color = (0,0,0)
    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

        if(self.x>self.y):
            self.label = 1

        else:
            self.label = -1
        self.color = (255, 0, 0)