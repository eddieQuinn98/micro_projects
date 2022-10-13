"""
Original KATA: https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
Date: 03 - 10 - 22

This is a messay way of doing it, but i think a class would of been the tidiest way of doing this.
I would like to make the following changes
    - The object returns the deadfish when called, rather than having to realy on the loop()
"""


class deadfish():

    def __init__(self, data):
        self.dict = {"i":self.i, "d":self.d, "s":self.s, "o":self.o}
        self.data = [*data]
        self.cv = 0
        self.deadfish = []

    def loop(self):
        for o in self.data:
            try: self.dict[o]()
            except KeyError: continue
        return self.deadfish
    
    def i(self):self.cv += 1
    def d(self):self.cv -= 1
    def s(self):self.cv **= 2
    def o(self):self.deadfish.append(self.cv)

def parse(data):
    Deadfish = deadfish(data)
    return Deadfish.loop()

if __name__ == "__main__":
    print(parse("codewards"))
        