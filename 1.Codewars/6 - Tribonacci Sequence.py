"""
KATA LINK: https://www.codewars.com/kata/556deca17c58da83c00002db/solutions/python
DATE: 30/10/22
"""

def tribonacci(signature:list, n:int) -> list:
    i = 3
    while (i) < n:
        signature.append(sum(signature[i-3:i]))
        i += 1
    return signature[:n]
    
if __name__ == "__main__":
    print(tribonacci([1, 1, 1], 10))