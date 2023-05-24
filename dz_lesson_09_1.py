class Simple_Car(object):
    def __init__(self, mark, color, v_dvyguna):
        self.mark = mark
        self.color = color
        self.v_dvyguna = v_dvyguna
    def ahead(self):
        return f"Car {self.mark} goes ahead"
    def back(self):
        return f"Car {self.mark} goes back"

class Difficult_Car(Simple_Car):
    def turn_left(self):
        return f"Car {self.mark} turns left"
    def turn_right(self):
        return f"Car {self.mark} turns right"

my_own_car = Simple_Car('Toyota','red','2')
print('My car is',my_own_car.color)
print(my_own_car.ahead())

husband_car = Difficult_Car('Volskvagen','black','2.4')
print('My husband car is',husband_car.color)
print(husband_car.turn_right())
