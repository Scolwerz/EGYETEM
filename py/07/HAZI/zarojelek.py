#!/usr/bin/env python3

def test(expression):
    stack = []
    openings = "([{"
    closings = ")]}"

    for c in expression:
        if c in openings:
            stack.append(c)
        elif c in closings:
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and c != ')') or (top == '[' and c != ']') or (top == '{' and c != '}'):
                return False

    if stack:
        return False

    return True


def main():
    print(test("((5+3)*2+1)"))  # True
    print(test("{[(3+1)+2]+}"))  # True
    print(test("(3+{1-1)}"))     # False
    print(test("[1+1]+(2*2)-{3/3}"))  # True
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))  # False

###################################################

if __name__ == "__main__":
    main()
