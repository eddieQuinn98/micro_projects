def beeramid(bonus:int, price:int):
    remaining_cans = bonus//price
    level = 0
    while (level+1)**2 <= remaining_cans:
        remaining_cans = remaining_cans - (level+1)**2
        level = level + 1
    return level        


if __name__ == "__main__":
    print(beeramid(21, 1.5))