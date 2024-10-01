class Vector2D():
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return("x {}, y {}".format(self.x,self.y))