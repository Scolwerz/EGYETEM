#!/usr/bin/env python3


def create_empty_file(filename, content=""):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Created {filename} successfully.")
    else:
        print(f"Error: {filename} already exists.")


def main():
    while True:
    print('''
---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
q) quit
'''.strip())
    choice = input("> ").lower()
    
    if choice == "1" or choice == "py":
        create_empty_file("alap.py", '''
#!/usr/bin/env python3

def main():
    print('Py3')

if __name__ == "__main__":
    main()
'''.strip())
    elif choice == "2" or choice == "c":
        create_empty_file("alap.c", '''
#include <stdio.h>

int main()
{
    printf("Hello World!\n");

    return 0;
}
'''.strip())
    elif choice == "q" or choice == "quit":
        break
    else:
        print("Invalid choice. Please choose again.")

#############################################################################

if __name__ == "__main__":
    main()
