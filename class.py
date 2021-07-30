class someclass:
    def __init__(self, car, color, year):
        self.car = car
        self.color = color
        self.year = year

    def introduce_self(self):
        print("My favorite car is a " + self.color + self.car + "from the year " + self.year)


car1 = someclass("Corvette", "blue", "2021")
car2 = someclass("Mustang", "silver", "2016")

car1.introduce_self()
car2.introduce_self()
