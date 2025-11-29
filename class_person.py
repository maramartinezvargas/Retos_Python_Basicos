#!/usr/bin/env python3

"""
### **13. Clase Persona**

**Fichero:** `class_person.py`

Define una clase `Person` con los atributos `name` y `age`. 
Añade un método `introduce()` que muestre un mensaje utilizando ambos atributos.
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"¡Hola! Soy {self.name} y tengo {self.age} años.")  

p = Person("Mara",36)
p.introduce()
