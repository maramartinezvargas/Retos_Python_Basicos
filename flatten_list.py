#!/usr/bin/env python3

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