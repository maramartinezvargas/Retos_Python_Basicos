#!/usr/bin/env python3

def fizz_buzz():
    for i in range (1,51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    fizz_buzz()
    
if __name__ == "__main__":
    main()
    