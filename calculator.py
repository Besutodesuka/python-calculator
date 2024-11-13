class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # fix the order b- a -> a-b
        return a - b

    def multiply(self, a, b):
        result = 0
        # fix number of iteration b+1 -> b
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = 0
        temp_a,temp_b = a,b
        while abs(a) >= abs(b):
            a = self.subtract(a, b) if a > 0 else self.add(a, b)
            if (temp_a >= 0 and temp_b >= 0) or (temp_a < 0 and temp_b < 0):
                result += 1
            else:
                result -= 1
        return result  # Adjust sign based on a
    
    def modulo(self, a, b):
        # fix operation <= -> >=
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))