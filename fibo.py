def fibonacci(n):
    fib_seq = [0, 1]  # Starting values for Fibonacci series
    for i in range(2, n):
        next_num = fib_seq[-1] + fib_seq[-2]  # Sum of last two elements
        fib_seq.append(next_num)
    return fib_seq

# Example usage
n = int(input("Enter the number of terms: "))
fib_series = fibonacci(n)
print(f"Fibonacci series: {fib_series}")
