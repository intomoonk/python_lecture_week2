def fibo(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


n = 10
fib_seq = fibo(n)
print(fib_seq)