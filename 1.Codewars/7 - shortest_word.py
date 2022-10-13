"""
Original codewars challenge: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python
Date: 18-06-22
"""

def find_short(s):
    shortest_length = None
    for word in s.split():
        if shortest_length == None or len(word) < shortest_length:
            shortest_length = len(word)
    return shortest_length

if __name__ == "__main__":
    find_short("bitcoin take over the world maybe who knows perhaps")