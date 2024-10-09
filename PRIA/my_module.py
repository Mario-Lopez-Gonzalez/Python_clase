import math

class Vector2D():
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return("({},{})".format(self.x,self.y))
    
    def module(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def scalar_prod(self, r = 1):
        return Vector2D(self.x*r,self.y*r)
    
    @staticmethod
    def sum(vec1,vec2):
        return Vector2D((vec1.x+vec2.x),(vec1.y+vec2.y))
    
    @staticmethod
    def substract(vec1,vec2):
        return Vector2D((vec1.x-vec2.x),(vec1.y-vec2.y))

class Vector3D(Vector2D):
    z = 0

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return("({},{},{})".format(self.x,self.y,self.z))
    
    def module(self):
        return math.sqrt(super().module()+self.z**2)
    
    def scalar_prod(self, r=1):
        return Vector3D(self.x*r,self.y*r,self.z*r)
    
    @staticmethod
    def sum(vec1,vec2):
        return Vector3D((vec1.x+vec2.x),(vec1.y+vec2.y),(vec1.z+vec2.z))

    @staticmethod
    def substract(vec1,vec2):
        return Vector3D((vec1.x-vec2.x),(vec1.y-vec2.y),(vec1.z-vec2.z))

    @staticmethod
    def dot_product(vec1,vec2):
        return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z
    
    @staticmethod
    def distance(vec1,vec2):
        temp = Vector3D.substract(vec1,vec2)
        return math.sqrt(temp.x**2 + temp.y**2 + temp.z**2)