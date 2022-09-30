"""
KATA LINK: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
DATE: 09/06/22
"""

def solution(s):
    return "".join(l if l.islower() else f" {l}" for l in list(s))

if __name__ == "__main__":
    print(solution("helloWorld"))
    print(solution("breakCamelCase"))