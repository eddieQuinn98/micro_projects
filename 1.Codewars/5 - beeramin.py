def beeramid(bonus:int, price:int):
    remaining_cans = bonus//price
    level = 0
    while (level+1)**2 <= remaining_cans:
        remaining_cans = remaining_cans - (level+1)**2
        level = level + 1
    return level        


if __name__ == "__main__":
    print(beeramid(21, 1.5))
    """print(beeramid(10, 2))
    print(beeramid(11, 2))
    print(beeramid(21, 1.5))
    print(beeramid(454, 5))
    print(beeramid(455, 5))
    print(beeramid(4, 4))
    print(beeramid(3, 4))
    print(beeramid(0, 4))
    print(beeramid(-1, 4))"""