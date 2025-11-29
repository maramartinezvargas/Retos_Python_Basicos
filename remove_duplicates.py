#!/usr/bin/env python3

def remove_duplicates(data):
    
    new = []
    
    for e in data:
        if e not in new:
            new.append(e)

    return new

data = [1,1,25,2,56,35,3,2,56]
print(data)
print(remove_duplicates(data))
