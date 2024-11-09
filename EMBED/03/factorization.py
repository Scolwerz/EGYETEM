from time import time

def factorization(n):
    factors = []
    for i in range(2, n//2+1):
        if n % i == 0:
            factors.append(i)
    return factors


def main():
    n = int(input("N: "))

    start = time()
    factors = factorization(n)
    end = time()

    print(factors)
    print(f"Elapsed time: {end - start} seconds")


if __name__ == "__main__":
    main()
