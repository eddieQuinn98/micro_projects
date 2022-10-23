"""
KATA LINK: https://www.codewars.com/kata/5254ca2719453dcc0b00027d/solutions/python
date: 23/10/22

Would of like to do with without relying on itertools, but im not good enough at recursion to do that yet. Will come back to at a later date
"""

import itertools


def permutations(s):
    raw_l = [("".join(l for l in i))
             for i in list(itertools.permutations([*s]))]
    return list(dict.fromkeys(raw_l))


if __name__ == "__main__":
    print(permutations('aabb'))
