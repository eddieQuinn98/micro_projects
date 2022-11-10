def fizzbuz(max: int = 100, tests: dict = {3: "fizz", 5: "buzz"}):
    for i in range(1, max+1):
        r = "".join(tests[t] if i % t == 0 else "" for t in tests)
        print(i if r == "" else r)


if __name__ == "__main__":
    i = int(input(("please enter the number you want to go up to:\n")))
    fizzbuz(i)
