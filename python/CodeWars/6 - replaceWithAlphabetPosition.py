"""
KATA: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
Date: 06/10/22
"""

def alphabet_position(text:str):
    d = {chr(i+96):i for i in range(1,27)}
    os = []
    for l in [*text.lower()]:
        try: os.append(str(d[l]))
        except KeyError: continue
    return ' '.join(os)

if __name__ == "__main__":
    print(alphabet_position("yeet"))
    print(alphabet_position("The sunset sets at twelve o' clock."))
    