class Calculator:
    def calculate(self, a, b, op):
        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            return a / b
        else:
            return "Invalid operation"

calc = Calculator()


a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/sub/mul/div): ")

print(calc.calculate(a, b, op))
