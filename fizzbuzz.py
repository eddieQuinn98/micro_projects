def check(inp: int, test: int):
    return inp % test == 0


def fizzbuz(max: int = 100, tests: dict = {3: "fizz", 5: "buzz"}):
    for num in range(1, max):
        response = ""
        for test in tests:
            response += tests[test] if check(num, test) else ""
        print(num) if response == "" else print(response)


i = input("please enter the number you want to go up to:\n")
if i:
    try:
        fizzbuz(int(i))
    except ValueError:
        print("Please enter valid number")
