# Un string es un conjunto de caracteres que se encierran en comillas dobles o simples.
from typing import Tuple

mi_string = "Hola, esto es un string"
mi_string = " Este es un string \n que contiene saltos de linea\n como podes ver, "

print(mi_string)
# Resultado => Este es un string
# Resultado =>  que contiene saltos de linea
# Resultado => como podes ver,

# =====================================
# ==== FORMATEANDO UN TEXTO ===========

lenguaje = "Python 3"
nombre = "Santiago"

# teniendo esas 2 variables podemos formar un texto de las siguientes maneras:

mensaje_1= "Aprendiendo " + lenguaje + " con "+ nombre
mensaje_2= "Aprendiendo %s con %s" %(lenguaje,nombre)
mensaje_3= "Aprendiendo {} con {} ".format(lenguaje,nombre)


print(mensaje_1)
# Resultado => Aprendiendo Python 3 con Santiago
print(mensaje_2)
# Resultado => Aprendiendo Python 3 con Santiago
print(mensaje_3)
# Resultado => Aprendiendo Python 3 con Santiago

''' Como pueden ver los 3 mensajes dan el mismo resultado pero lo hicimos de distintas maneras.
La forma básica y que primero se aprende es con el + colocando las variables fuera de las comillas y el texto fijo entre
comillas.
La segunda forma es con los símbolos "%s" que suplantarían a las variables. (Nota: A partir de python 3 se recomienda 
el uso de format()).
Y finalmente tenemos la función format() que nos permite hacer múltiples sustituciones, esto es epecialmente bueno 
cuando trabajamos con largas listas o tuplas.
con format() Se pueden combinar arbitrariamente argumentos posicionales y nombrados:
Ejemplo:
'''
print("La historia de {0}, {1} y {otro}.".format('Juan', 'Jose', otro='Luis'))
# Resultado => La historia de Juan, Jose y Luis.

print("Mis mascotas son un {}, un {} y un {}".format('Perro', 'Gato', 'Hamster'))

# Resultado => Mis mascotas son un Perro, un Gato y un Hamster

# Esto último podemos optimizarlo de esta forma:

mascotas = ['Perro', 'Gato', 'Hamster']

print("Mis mascotas son un {}, un {} y un {}".format(*mascotas))

# Resultado => Mis mascotas son un Perro, un Gato y un Hamster

