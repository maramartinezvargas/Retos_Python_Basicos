#!/usr/bin/env python3

def dict_sum_values(data):
    
    total = 0
    for value in data.values():
        total += value
    print(total)

data = {
    "a": 5, 
    "b":10,
    "c":15,
    "d":3
    }

dict_sum_values(data)