#!/usr/bin/env python3

def invert_dict(data):
    
    new = {}
    
    for key, value in data.items():
        new[value] = key
    
    return new


data ={
    "Nombre" : "Mara",
    "Apellido" : "Martinez",
    "Ciudad" : "Madrid"
}

print(invert_dict(data))