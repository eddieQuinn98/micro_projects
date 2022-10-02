"""
Original codewars challenge: https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
date: 22/09/22
"""

def cakes(recipe, available):
    try:
        return_val = min(int(available[x]/recipe[x]) for x in recipe.keys())
    except KeyError:
        return_val = 0
    return return_val


if __name__=="__main__":
    recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
    available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe1, available1))

    recipe2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available2 = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe2, available2))
    
