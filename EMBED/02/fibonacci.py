
def main():
    a, b = 0, 1
    for _ in range(10):
        print(a, end=' ')
        a, b = b, a+b

if __name__ == "__main__":
    main()