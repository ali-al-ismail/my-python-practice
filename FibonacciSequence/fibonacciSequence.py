def fibonacciSequence(n):
    if n == 0 or n == 1:
        return n
    return fibonacciSequence(n-1) + fibonacciSequence(n-2)
