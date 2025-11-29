#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2. Filtrar números pares
Dada una lista de números enteros, genera una nueva lista que contenga únicamente los números pares utilizando comprensión de listas (list comprehension).
"""

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [n for n in nums if n % 2 == 0]

print("Lista original: ", nums)
print("\nLista por comprensión: ", result)