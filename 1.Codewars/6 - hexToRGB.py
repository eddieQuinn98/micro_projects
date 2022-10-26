"""
KATA LINK: https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/solutions/python
DATE: 25/10/22
"""

def hex_string_to_RGB(hex_string:str):
    hex_string = hex_string[1:] if hex_string[0] == '#' else hex_string
    return {i[0]:int(hex_string[i[1]:i[1]+2], 16) for i in (("r",0),("g",2),("b",4))}

if __name__ == "__main__":
    print(hex_string_to_RGB("#FF9933"))