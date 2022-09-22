"""
Original codewars challenge: https://www.codewars.com/kata/5264d2b162488dc400000001
Date: 18-06-22
"""


def flip_word(word: str):
    new_word = ""
    for letter in word[::-1]:
        new_word = new_word + letter
    return new_word


def spin_words(sentence: str, word_length: int = 5):
    new_sentence = ""
    sentence_as_list = sentence.split()
    position = 0
    for word in sentence_as_list:
        spacing = "" if (position+1) == len(sentence_as_list) else " "
        new_sentence += flip_word(word) + \
            spacing if len(word) > (word_length-1) else word + spacing
        position = position + 1
    return new_sentence


if __name__ == "__main__":
    returned_val = spin_words("Hey wollef sroirraw")
    print(returned_val)
