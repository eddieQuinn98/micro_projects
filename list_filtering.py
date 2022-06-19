"""
KATA LINK: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/
DATE: 09/06/22

DESC: In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""


def filter_list(l):
    return [item for item in l if type(item) != str]


if __name__ == "__main__":
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 'a', 'b', 0, 15]))
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))
