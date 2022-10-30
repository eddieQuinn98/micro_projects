"""
KATA LINK: https://www.codewars.com/kata/515bb423de843ea99400000a/solutions/python
DATE: 26/10/22

I could of done certain aspects of this better - namingly the page index
"""


class PaginationHelper:

    def __init__(self, c: list, n: int):
        self.c = c
        self.n = n
        self._split_list = [self.c[i:i+self.n]
                            for i in range(0, len(self.c), self.n)]
        self.dict = {self._split_list.index(i): i for i in self._split_list}

    def item_count(self):
        return len(self.c)

    def page_count(self):
        return len(self.dict)

    def page_item_count(self, page_index: int):
        try:
            r_val = len(self.dict[page_index])
        except KeyError:
            r_val = -1
        return r_val

    def page_index(self, item_index: int):
        if item_index < 0 or item_index > (self.item_count()-1):
            return -1
        for p in self.dict:
            if self.c[item_index] in self.dict[p]:
                return p


if __name__ == "__main__":
    helper = PaginationHelper(list(range(1, 25)), 10)

    print(helper.page_count())
    print(helper.item_count())

    print(
        helper.page_item_count(0),
        helper.page_item_count(1),
        helper.page_item_count(2),
        helper.page_item_count(3))

    print(
        helper.page_index(5),
        helper.page_index(2),
        helper.page_index(20),
        helper.page_index(-10),
        helper.page_index(25)
    )
