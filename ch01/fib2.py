def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


if __name__ == "__main__":
    print(fib2(4))

# fib(4) =>  fib(3) => fib(2) => fib(1) => 1
#                             => fib(0) => 0
#                   => fib(1) => 1
#            fib(2) => fib(1) => 1
#                      fib(0) => 0
