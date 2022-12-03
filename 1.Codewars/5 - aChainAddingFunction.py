class add(int):
    def __call__(self, v):
        return add(self + v)


if __name__ == "__main__":
    print(add(1)(2))
