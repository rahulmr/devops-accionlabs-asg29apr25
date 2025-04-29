class FibonacciCalculator:
    def __init__(self):        
        self.a = 0
        self.b = 1

    def next_fibonacci(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def sum_even_fibonacci(self, count):
        even_sum = 0
        even_count = 0

        while even_count < count:
            fib = self.next_fibonacci()
            if fib % 2 == 0:
                even_sum += fib
                even_count += 1

        return even_sum


if __name__ == "__main__":
    calculator = FibonacciCalculator()
    result = calculator.sum_even_fibonacci(100)
    print(f"The sum of the first 100 even-valued Fibonacci numbers is: {result}")