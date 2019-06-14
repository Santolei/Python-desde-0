# ==========================================================================================
# ==== TIPOS DE DATOS ======================================================================

# =====================================
# ==== NÚMEROS =========================
# Enteros, flotantes, complejos
a = -4
b = 2.3302
c = 2.1 + 6j

print("Entero:", a)
print("Flotante:", b)
print("Complejo:", c)

# Resultado => Entero: -4
# Resultado => Flotante: 2.3302
# Resultado => Complejo: (2.1+6j)

print("El numero 1 es", a)
# Resultado => El numero 1 es -4

print("El numero 2 es", b)
# Resultado => El numero 2 es 2.3302

resultado = a + b

print("La suma de ambos es", resultado)
# Resultado => La suma de ambos es -1.6698

# =====================================
# ==== LISTAS =========================
# Son un conjunto ordenado de ítems. Dichos items no tienen que ser necesariamente del mismo tipo.
# Declarar una lista es muy similar a otros lenguajes de programación, el contenido debe estar entre "[]" y separado por comas.
# EJEMPLO:

lista = [1, 2, 3, "Manzana", True]

print("Lista:", lista)

# Resultado => Lista: [1, 2, 3, 'Manzana', True]

# Podemos acceder a cada uno de los ítems de la siguiente manera:

print(lista[3])
# Resultado => Manzana

print("El primer ítem es:", lista[0])

# Resultado => El primer ítem es:  1

print("El quinto ítem es:", lista[4])

# Resultado => El quinto ítem es:  True

# =====================================
# ==== TUPLAS =========================

# Las tuplas son son una secuencia de ítems similar a las listas. Lo que las diferencia es que las tuplas son permantenes.
# <=<=<= IMPORTANTE =>=>=>
# Una vez generadas no pueden ser modificadas. Se suelen usar para proteger datos contra escritura y son más rápidas que las listas dado que no cambian dinámicamente.
# Se definen con "()" (parentesis) y separadas por comas.
# EJEMPLO:

tupla = (23, "Santiago", [123, 22, 33])

print("Tupla:", tupla)

# Resultado => Tupla: (23, 'Santiago', [123, 22, 33])

# Se puede acceder a las tuplas con [] al igual que en las listas pero no se pueden modificar esos datos:

print("Mi nombre es:", tupla[1])

# Resultado => Mi nombre es: Santiago

# =====================================
# ==== CADENAS O STRINGS ==============

str = "Esto es un string"
print(str)
# Resultado => Esto es un string

# =====================================
# ==== BOOLEANOS ======================
# True o False

x = True
y = False

print("X:", x)

# Resultado => X: True

# =====================================
# ==== CONJUNTOS O SETS ===============

# Un conjunto es una colección no ordenada de objetos únicos.
# Para crear un conjunto especificamos sus elementos entre llaves:

set1 = {True, 3.14, None, False, "Hola mundo", (1, 2)}

# Se pueden hacer operaciones como uniones o intersecciones entre 2 sets, como tienen valores únicos se eliminan los duplicados.

set2 = {1,1,3,"a", 3, "a"}

print(set2)

# Resultado => {1, 3, 'a'} Se eliminaron los duplicados :)

#Vamos a hacer una union:

set3 = {1,2,3,4}
set4 = {4,5,6,7,8}

print(set3 | set4)
# Resultado => {1, 2, 3, 4, 5, 6, 7, 8}

#Ahora una intersección:

print(set3 & set4)

# Resultado => {4}

# =====================================
# ==== DICCIONARIOS =================== #
# Son estructuras de datos con características especiales que nos permiten almacenar cualquier tipo de valor.
# Estos diccionarios nos permiten identificar cada elemento por una clave (key).

diccionario = {'nombre': 'Santiago', 'edad': 30, 'habilidades': ['Python', 'Php', 'JavaScript', 'Jiu-jitsu']}

print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['habilidades'])

# Resultado => Santiago
# Resultado => 30
# Resultado => ['Python', 'Php', 'JavaScript', 'Jiu-jitsu']

# ==========================================================================================
# ==== VARIABLES ===========================================================================

# Pasamos a otro tema, las variables en python no necesitan ser declaradas como en otros lenguajes de programación.
# para generar una variable le asignamos un valor y comenzamos a usarla. Así de simple. los valores se asignan con "="

variable1 = 123

print(variable1)
# Resultado => 123

# si cambiamos el valor de la variable y la usamos de nuevo el valor será sustituido:

variable1 = 200

print(variable1)
# Resultado => 200

# Python también nos permite asignar el mismo valor a varias variables al mismo tiempo:

a = b = c = 300

print(a,b,c)
# Resultado => 300 300 300

# =====================================
# ==== TIPOS DE VARIABLES =============

# En muchos lenguajes de programación las variables van de acuerdo a los tipos. eso indica que una variable es declarada
# inicialmente para tener un tipo particular y siempre será el mismo.
# Las variables en python no están sujetas a esa restricción:

var = 23.5
print(var)
# Resultado => 23.5

var = "Ahora soy un string"
print(var)
# Resultado => Ahora soy un string

