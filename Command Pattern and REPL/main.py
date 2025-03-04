class Command:
    def execute(self):
        raise NotImplementedError

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

def repl():
    while True:
        try:
            command = input("Enter command (add/subtract): ").strip().lower()
            if command == "exit":
                break
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if command == "add":
                cmd = AddCommand(a, b)
            elif command == "subtract":
                cmd = SubtractCommand(a, b)
            else:
                print("Invalid command")
                continue

            result = cmd.execute()
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    repl()
