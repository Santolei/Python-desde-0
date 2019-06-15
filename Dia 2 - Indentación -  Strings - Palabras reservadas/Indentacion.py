'''
La indentación (o dejar un espacio en blanco o sangría) es una de las características más remarcables de Python
(y una de las causas más comunes por las que nos salga un error)
En Python, las líneas de código que están dentro de un mismo
deben estar agrupadas, teniendo el mismo número de espacios a la izquierda de cada línea
Por ejemplo:
'''

# Carrefour
#   Carnicería
#       Cerdo
#       Pollo
#   Pescadería
#       Atún
# Coto
#   Verdulería
#       Peras
#       Manzanas

# pero si lo hicieramos de esta manera estaría mal y no daría un error:

# Coto
#   Verdulería
#       Peras
#   Manzanas

'''
como podemos ver "Manzanas" está al mismo nivel que "verdulería" y cuando debería tener un nivel inferior
(yo lo pienso como que está dentro de verdulería)
'''

# Veamos un ejemplo con un IF (Si no sabes lo que es un if, no te preocupes que ya vamos a llegar)

x = 6
if x > 5:
    print("X es más grande que 5")

# Resultado => X es más grande que 5

# Como podemos ver solo se va a imprimir en pantalla el resultado siempre que x sea mayor a 5 pero si lo indentamos
# de esta manera va a dar error:

x = 6
if x > 5:
print("X es más grande que 5")
# Resultado => IndentationError: expected an indented block

'''
Otro posible error:
IndentationError: unexpected indent
Estos son unos de lo errores más comunes de python asique acostumbrate a verlos seguido, cuando los veas es porque
tuviste algun error al indentar
'''
