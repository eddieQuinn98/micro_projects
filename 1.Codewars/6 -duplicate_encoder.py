"""
KATA LINK: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/pythonhttps://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
DATE: 21/09/22

Notes: I would of liked to of used dictionary comprehension here rather than relying on a whole for loop.
"""

def duplicate_encode(word):
    letter_list = list(word.lower())
    letter_count = {}
    output_str = ""
    for letter in letter_list:
        letter_count[letter] = True if letter in letter_count.keys() else False
    for letter in letter_list:
        output_str += ")" if letter_count[letter] == True else "("
    return output_str


if __name__=="__main__":
    new_str = duplicate_encode("abdfffer")
    print(new_str)