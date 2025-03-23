class Vector:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __hash__(self):
        return hash((self.x, self.y))
    