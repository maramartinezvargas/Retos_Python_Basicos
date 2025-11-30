#!/usr/bin/env python3

def is_palindrome(string):
    aux = string.lower().replace(" ", "")
    rev = aux[::-1]
    return aux == rev

string = "anita lava la tina"
if is_palindrome(string): 
    print(string, "SI es palindroma")
else:
    print(string, "NO es palindroma")
