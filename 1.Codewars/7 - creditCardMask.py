"""
KATA LINK: https://www.codewars.com/kata/5412509bd436bd33920011bc/solutions/python
DATE: 30/10/22

This could of been done better, i didnt have to force the items into a list for one. Also for the first section
I could of just done `#`*len(cc)-4). I think this is an important lesson in K.I.S.S
"""

def maskify(cc):
    return "".join("#" for c in [*str(cc)][:-4]) + "".join(c for c in [*str(cc)][-4:])

if __name__ == "__main__":
    maskify(123456789)