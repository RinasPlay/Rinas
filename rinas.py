class Stul:

    def __init__(self, count, material, figure):
        self.count = count
        self.material = material
        self.figure = figure


    def __str__(self):
        return "Стул" + " " + "(" + self.count.__str__() + ", " + self.material + ", " + self.figure + ")"

    def __repr__(self):
        return "Стул" + " " + "(" + self.count.__str__() + ", " + self.material + ", " + self.figure + ")"

chair = Stul(3, "iron", "circle")

print(chair)


