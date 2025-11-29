
# **Retos Python Básicos — Colección de ejercicios para desarrollar habilidades prácticas**

Este repositorio reúne una selección de 15 ejercicios de Python pensados para mejorar de forma progresiva el razonamiento, la lógica y el dominio de las estructuras fundamentales del lenguaje. Cada reto está diseñado para practicar conceptos clave de programación y para demostrar un enfoque claro, ordenado y eficaz a la hora de resolver problemas reales.

Mi objetivo al construir este repositorio es ir ampliando y practicando habilidades en Python, manteniendo buenas prácticas y código limpio. Además, sirve como referencia para cualquier persona que quiera repasar fundamentos o ver ejemplos de soluciones limpias a problemas comunes.

---

# **Enunciados de los 15 ejercicios**

---

### **1. Contador de palabras**

**Fichero:** `word_counter.py`

Escribe una función que reciba un texto y devuelva un diccionario donde las claves sean las palabras y los valores el número de veces que aparece cada una de ellas. Ignora mayúsculas/minúsculas.

---

### **2. Filtrar números pares**

**Fichero:** `filter_even_numbers.py`

Dada una lista de números enteros, genera una nueva lista que contenga únicamente los números pares utilizando comprensión de listas.

---

### **3. Máximo y mínimo sin funciones built-in**

**Fichero:** `manual_max_min.py`

Dada una lista de números, calcula el valor máximo y el mínimo sin utilizar las funciones `max()` ni `min()`.

---

### **4. Comprobar si una palabra es palíndroma**

**Fichero:** `is_palindrome.py`

Implementa una función que determine si una palabra o frase es un palíndromo. No debe tener en cuenta espacios ni mayúsculas.

---

### **5. Eliminar elementos duplicados**

**Fichero:** `remove_duplicates.py`

Crea una función que reciba una lista y devuelva una nueva lista con los elementos únicos, manteniendo cualquier orden válido.

---

### **6. FizzBuzz**

**Fichero:** `fizzbuzz.py`

Escribe un programa que imprima los números del 1 al 50.

* Si el número es múltiplo de 3, imprime “Fizz”.
* Si es múltiplo de 5, imprime “Buzz”.
* Si es múltiplo de ambos, imprime “FizzBuzz”.

---

### **7. Sumar valores de un diccionario**

**Fichero:** `dict_sum_values.py`

Dado un diccionario cuyas claves son cadenas y cuyos valores son números, implementa una función que calcule la suma total de esos valores.

---

### **8. Contador de vocales**

**Fichero:** `count_vowels.py`

Escribe una función que reciba una cadena de texto y devuelva cuántas vocales contiene (a, e, i, o, u), sin diferenciar mayúsculas de minúsculas.

---

### **9. Frecuencia de caracteres**

**Fichero:** `char_frequency.py`

Implementa una función que reciba una cadena de texto y genere un diccionario que indique cuántas veces aparece cada carácter individual.

---

### **10. Invertir un diccionario**

**Fichero:** `invert_dict.py`

Crea una función que reciba un diccionario y devuelva uno nuevo donde las claves sean los valores originales y los valores sean las claves. Supón que los valores no están repetidos.

---

### **11. Análisis básico de un fichero de texto**

**Fichero:** `file_basic_analysis.py`

Escribe un programa que abra un fichero de texto y muestre:

1. El número total de líneas.
2. El número total de palabras.
3. La palabra que se repite con más frecuencia.

---

### **12. Aplanar una lista**

**Fichero:** `flatten_list.py`

Dada una lista que contiene listas internas (por ejemplo `[1, [2, 3], [4, 5]]`), implementa una función que devuelva una lista “aplanada” en un único nivel.

---

### **13. Clase Persona**

**Fichero:** `class_persona.py`

Define una clase `Persona` con los atributos `nombre` y `edad`. Añade un método `presentarse()` que muestre un mensaje utilizando ambos atributos.

---

### **14. Implementar un CRUD sencillo**

**Fichero:** `simple_crud_manager.py`

Crea una clase que gestione una lista de elementos y permita realizar estas operaciones:

* añadir un elemento,
* eliminar un elemento,
* comprobar si un elemento existe,
* listar todos los elementos almacenados.

---

### **15. Consumir una API pública**

**Fichero:** `consume_public_api.py`

Implementa una función que realice una petición GET a la API:

`https://api.agify.io/?name=<nombre>`

y devuelva la edad estimada para el nombre proporcionado.

---
Perfecto. Aquí tienes una **sección final de “Conceptos básicos de Python”**, pensada para complementar tus ejercicios y reforzar lo que una persona debe conocer para resolverlos. Es clara, útil y encaja perfectamente en un README orientado a aprendizaje continuo.

Puedes pegarla tal cual al final del documento.

---

# **Conceptos básicos necesarios para resolver estos ejercicios**

Esta sección recopila los fundamentos de Python que resultan más útiles para abordar los retos de este repositorio. Sirve como guía rápida tanto para repasar conceptos como para profundizar en ellos mientras se practica.

---

## **1. Tipos de datos fundamentales**

### **Numéricos**

* `int`: números enteros
* `float`: números decimales

### **Texto**

* `str`: cadenas de texto
  Métodos frecuentes: `.lower()`, `.upper()`, `.split()`, `.strip()`, `.replace()`

### **Colecciones**

* `list`: ordenadas, mutables
* `tuple`: ordenadas, inmutables
* `dict`: pares clave–valor
* `set`: colecciones sin duplicados

---

## **2. Estructuras de control**

### **Condicionales**

```python
if condicion:
    ...
elif otra_condicion:
    ...
else:
    ...
```

### **Bucles**

* `for` para iterar sobre listas, strings, diccionarios…
* `while` cuando necesitas repetir hasta que algo cambie

Palabras clave útiles: `break`, `continue`, `range()`

---

## **3. Comprensiones (muy útiles en Python)**

### **List comprehension**

```python
[n for n in lista if n % 2 == 0]
```

### **Dict comprehension**

```python
{k: len(k) for k in palabras}
```

---

## **4. Funciones**

Cómo definir funciones:

```python
def nombre_funcion(parametros):
    return algo
```

Conceptos clave:

* parámetros vs argumentos
* valores por defecto
* return
* scope de variables

---

## **5. Manejo básico de ficheros**

```python
with open("archivo.txt", "r") as f:
    contenido = f.read()
```

Modos típicos:

* `"r"` leer
* `"w"` escribir
* `"a"` añadir
* `"rb"` leer binario

Funciones frecuentes:

* `.read()`
* `.readlines()`
* iteración línea a línea

---

## **6. Diccionarios: claves y valores**

Métodos clave:

* `.keys()`
* `.values()`
* `.items()`
* `.get(clave, valor_por_defecto)`

Son esenciales para ejercicios de conteo y análisis.

---

## **7. Manejo de errores**

```python
try:
    ...
except FileNotFoundError:
    ...
except Exception as e:
    ...
finally:
    ...
```

Sirve para:

* ficheros inexistentes
* accesos inválidos
* evitar que un programa se rompa

---

## **8. Programación orientada a objetos (POO)**

Clase básica:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Conceptos:

* clases
* objetos
* atributos
* métodos
* `self`

---

## **9. Módulos y organización de código**

Importar módulos:

```python
import math
import random
from collections import Counter
```

Crear modularidad:

* separar ejercicios en ficheros
* mantener funciones aisladas
* usar nombres descriptivos

---

## **10. Consumo de APIs**

Paquete más común:

```python
import requests

r = requests.get("https://api.example.com")
data = r.json()
```

Conceptos básicos:

* endpoints
* JSON
* diccionarios resultantes
* códigos de estado (200, 400, 401, 500…)

---
