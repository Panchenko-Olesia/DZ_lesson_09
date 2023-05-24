class My_Car:
    def __init__(self, mark, color, v_dvyguna):
        self.mark = mark
        self.color = color
        self.v_dvyguna = v_dvyguna
def vpered(self):
    return f"Машина {self.mark} їде вперед"
def nazad(self):
    return f"Машина {self.mark} їде назад"

my_own_car = My_Car('Toyota','red','2')
print(my_own_car)
husband_car = My_Car('Volskvagen','black','2.4')
print(husband_car)
