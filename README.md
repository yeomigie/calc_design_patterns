This is an advanced command-line calculator implemented using the **Command Pattern** and **REPL** (Read, Evaluate, Print, Loop). It supports basic arithmetic operations: sum, difference, product, and quotient.

## Features
- Interactive REPL: Continuously takes user input and executes operations.
- Command Pattern: Each operation is encapsulated in a separate command class.
- Error Handling: Handles invalid inputs and division by zero gracefully.
- Commands Display: Displays supported operations when the user types `commands`.

## Commands
- `sum <num1> <num2>`: Adds two numbers.
- `difference <num1> <num2>`: Subtracts the second number from the first.
- `product <num1> <num2>`: Multiplies two numbers.
- `quotient <num1> <num2>`: Divides the first number by the second.
- `commands`: Displays supported operations.
- `exit`: Exits the calculator.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Sarachaker/calc_design_patterns.git
   cd calc_design_patterns
