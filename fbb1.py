import unittest

# 定義 Fibonacci 函數
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return 
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=', ')
        a, b = b, a+b
    print()

# 測試類別
class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), )
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_fib(self):
        # 這裡可以使用 io.StringIO 來捕獲輸出
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        fib(8)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "0, 1, 1, 2, 3, 5, 8")

if __name__ == '__main__':
    unittest.main()