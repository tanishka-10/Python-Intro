class Robot:
    def __init__(self, givenName, givenColor, givenWeight):
        self.color = givenColor
        self.name = givenName
        self.weight = givenWeight

    def introduce(self):
        print("My name is " + self.name)

r1 = Robot("mini-projects", "blue", 25)
r2 = Robot("anurag", "red", 200)

r1.introduce()
r2.introduce()

