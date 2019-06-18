# ==========================================================================================
# ==== CONDICIONALES =======================================================================

# =====================================
# ==== IF =============================

'''Solo ejecutará el código cuando la sentencia es verdadera: '''

numero = 5

if numero > 0:
    print(numero, "Es mayor que 0")
# Resultado => 5 Es mayor que 0

# =====================================
# ==== ELIF ===========================

'''La sentencia elifsignifica, "De lo contrario". Si no se cumple la expresión condicional se ejecuta el bloque 
de sentencias seguidas. '''

numero = -2

if numero > 0:
    print(numero, "Es mayor que 0")
elif numero < 0:
    print("Es menor")

# Resultado => Es menor

# =====================================
# ==== ELSE ===========================

''' La sentencia else, significa, De lo contrario. Se cumple cuando ninguna de los condicionales anteriores se ha 
cumplido.'''

numero = 0

if numero > 0:
    print(numero, "Es mayor que 0")
elif numero < 0:
    print("Es menor")
else:
    print("Es el Cero")

# Resultado => Es el Cero

# =====================================
# ==== CONDICIONALES ANIDADOS =========

''' if condición_1:
        bloque 1
else:
    if condición_2:
        bloque 2
    else:
        bloque 3 
'''
numero2 = -4
if numero2 > 0:
    print(numero2, "Es mayor que 0")
else:
    if numero2 < 0:
        print("Es menor o igual a 0")

# Resultado => Es menor o igual a 0