''' While es un ciclo o secuencia periódica que nos permite ejecutar código múltiples veces.

El ciclo while nos permite realizar múltiples iteraciones basándonos en el resultado de una expresión lógica
que puede tener como resultado un valor True o False.'''

# Ejemplo:
contador = 0
while contador < 5:
    print(contador)
    contador +=1

# Resultado => 01234

# =====================================
# ==== Ejercicio 1 ====================

''' Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10. 
Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. 
Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.'''

# Nota para leer un número usamos "input()"

numero = int(input("Ingrese un número menor a 10: => "))
while numero >= 10:
    numero = int(input("Ingrese un número menor a 10: => "))
print("El numero ingresado es: ", numero)

# =====================================
# ==== Ejercicio 2 ====================

''' Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número sea menor que 10, compruebe 
que se encuentre en el rango (0, 20).'''

numero = int(input("Ingrese un número menor o igual a 20 y mayor o igual que 0: => "))
while numero < 0 or numero > 20:
    numero = int(input("Ingrese un número menor o igual a 20 y mayor o igual que 0: => "))
print("El numero ingresado es: ", numero)

# =====================================
# ==== Ejercicio 3 ====================

''' Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un número de teclado y 
escriba el resultado por pantalla.'''

numero = int(input("Ingrese un número menor o igual a 20 y mayor o igual que 0: => "))
contador = 1
while numero < 0 or numero > 20:
    numero = int(input("Ingrese un número menor o igual a 20 y mayor o igual que 0: => "))
    contador +=1
print("El numero ingresado es: ", numero)
print("Cantidad de intentos: ", contador)