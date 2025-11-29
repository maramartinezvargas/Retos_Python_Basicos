#!/usr/bin/env python3

"""
9. Frecuencia de caracteres
Fichero: char_frequency.py

Implementa una función que reciba una cadena de texto y genere un diccionario que 
indique cuántas veces aparece cada carácter individual.
"""

def char_frequency(data):
    
    result = {}
    
    for c in data:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
            
    return result

data = "This is amazing"
print(char_frequency(data))