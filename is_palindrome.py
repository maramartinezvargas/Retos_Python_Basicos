#!/usr/bin/env python3

"""
4. Comprobar si una palabra es palíndroma
Fichero: is_palindrome.py

Implementa una función que determine si una palabra o frase es un palíndromo. No debe tener en cuenta espacios ni mayúsculas.
"""

def is_palindrome(string):
    aux = string.lower().replace(" ", "")
    rev = ""

    rev = aux[::-1]
    
    return aux == rev


string = "\"anita lava la tina\""

if is_palindrome(string): 
    print(string, "SI es palindroma")
else:
    print(string, "NO es palindroma")
