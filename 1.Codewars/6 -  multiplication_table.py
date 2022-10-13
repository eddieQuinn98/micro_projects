"""
Original KATA: https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
Data: 02-10-22

I could get this down to one lie but that would require me to calc xy twice, and i wanted to follow
dry principles
"""

def multiplication_table(size):
    xy = [n for n in range(1, size+1)]
    return [[y * x for x in xy] for y in xy]

if __name__ == "__main__":
    print(multiplication_table(5))