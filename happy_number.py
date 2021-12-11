max_loops = 100

def get_input():
    inpux_n = int(input("Please type in the number you want to test"))
    return inpux_n

def test_input(input_n):
    count = 0
    result = input_n
    while count is not max_loops:
        result = test(result)
        print(result)
        if result == 1:
            return True
        count = count + 1
    return False

def test(test):
    output = 0
    test = map(int, str(test))
    for number in test:
        output = output + number**2
    return output


if __name__ == "__main__":
    input_figure = get_input()
    result = test_input(input_figure)
    print(result)
