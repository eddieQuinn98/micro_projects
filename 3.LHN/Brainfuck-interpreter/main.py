class IncrementString:

    def __init__(self, input_str):
        self.input_str = input_str
        self.mem=[]
        self.output_str = ""
        self.pointer=0


        self.operators = {
            ">":self.increment_dp,
            "<":self.decrement,
            "+":self.increment,
            "-":self.decrement,
            ".":self.output_byte,
            ",":self.overwrite_byte,
            "[":self.open_square,
            "]":self.close_square
        }

    def operate(self):
        for o in self.input_str:
            try: self.operators[o]()
            except KeyError:
                print("Syntax error")
                break


    def increment_dp(self):
        self.pointer = self.pointer + 1

    def decrement_dp(self):
        self.pointer = self.pointer - 1

    def increment():
        """
        This needs to use the current pointer to get somthing inside the memory pool, and increment it by 1
        """
        pass

    def decrement():
        """
        This needs to use the current pointer to get somthing inside the memory pool, and decrement it by 1
        """
        pass

    def output_byte(self):
        self.output_str.join(self.mem[self.pointer])

    def overwrite_byte():
        pass

    def open_square():
        pass

    def close_square():
        pass


def INTERPRET(string_:str):
    """Takes in a string and interprets it"""
    for l in string_:
        print(l)



if __name__ == "__main__":
    print("Hello world")