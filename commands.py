class SumCommand:
    def execute(self, x, y):
        return x + y

class DifferenceCommand:
    def execute(self, x, y):
        return x - y

class ProductCommand:
    def execute(self, x, y):
        return x * y

class QuotientCommand:
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

class DisplayCommands:
    def execute(self):
        print("Supported operations: sum, difference, product, quotient")
