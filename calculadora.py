import argparse

class Calculator:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.memory = 0  # Atributo nuevo para guardar resultados

    def add(self, a, b):
        result = a + b
        if self.verbose:
            print(f"🧮 Adding {a} + {b} = {result}")
        else:
            print(result)
        self.memory = result

    def operate(self, operation=None, numbers=None):
        if not operation or not numbers:
            print("⚠️ No operation or numbers provided.")
            return

        a, b = numbers
        if operation == "add":
            self.add(a, b)
        else:
            print(f"🚧 Operation '{operation}' not implemented yet.")

    #def substract(a,b)
    #def multiply(a,b)
    #def divide(a,b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini Calculator CLI")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Math operation to perform")
    parser.add_argument("--numbers", nargs=2, type=float, help="Two numbers to operate with")
    args = parser.parse_args()

    calc = Calculator(verbose=args.verbose)
    calc.operate(operation=args.operation, numbers=args.numbers)
