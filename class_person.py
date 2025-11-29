#!/usr/bin/env python3

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"¡Hola! Soy {self.name} y tengo {self.age} años.")  

p = Person("Mara",36)
p.introduce()
