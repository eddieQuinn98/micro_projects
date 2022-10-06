"""
Orignal KATA: https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
Date: 06/10/2022
"""

def data_reverse(data:list, frame_length:int=8):
    rc = [data[x:x+frame_length] for x in range(0, len(data),8)][::-1]
    return [y for x in rc for y in x]


print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))