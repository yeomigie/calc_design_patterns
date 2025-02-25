from commands_v2 import SumCommand, DifferenceCommand, ProductCommand, QuotientCommand, DisplayCommands

# Command dictionary
actions = {
    "sum": SumCommand(),
    "difference": DifferenceCommand(),
    "product": ProductCommand(),
    "quotient": QuotientCommand(),
    "commands": DisplayCommands(),
}

def advanced_calculator():
    print("Welcome to Advanced Calculator. Type 'commands' for supported operations.")
    while True:
        user_input = input("Enter operation: ").strip().split()
        if user_input[0] == "exit":
            break
        try:
            action = actions[user_input[0]]
            if user_input[0] == "commands":
                action.execute()
            else:
                result = action.execute(float(user_input[1]), float(user_input[2]))
                print(f"Output: {result}")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}. Type 'commands' for help.")

if __name__ == "__main__":
    advanced_calculator()
