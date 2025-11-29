#!/usr/bin/env python3

"""
12. Aplanar una lista
Fichero: flatten_list.py

Dada una lista que contiene listas internas (por ejemplo [1, [2, 3], [4, 5]]), 
implementa una función que devuelva una lista “aplanada” en un único nivel.
"""

def flatten_list(data):
    
    flatten_data = []
    
    for items in data:
        if isinstance(items, list):
            flatten_data.extend(items)
        else:
            flatten_data.append(items)
    return flatten_data

data = [1, [2, 3], [4, 5]]
print(flatten_list(data))