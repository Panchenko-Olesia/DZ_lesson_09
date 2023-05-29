import math
class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        diagonal = math.sqrt(self.length**2 - self.width**2)
        sqr = diagonal * self.width
        return f"Площа параллелограма дорівнює {sqr}"

class Square (Parallelogram):
    def get_area(self):
        sqr = self.width * self.width
        return f"Площа квадрата дорівнює {sqr}"

my_paral = Parallelogram(8, 17)
print(my_paral.get_area())

my_square = Square(5,5)
print(my_square.get_area())