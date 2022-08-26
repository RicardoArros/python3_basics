# Lection 02

# Definir una tupla
fruits = ('Naranja', 'Platano', 'Guayaba')
print(fruits)

# Saber el largo
print(len(fruits))

# Acceder a un elemento
print(fruits[0])

# Navegacion inversa
print(fruits[-1])

# Acceder a un rango
print(fruits[0:1])

# Recorrer elementos
for fruit in fruits:
  print(fruit, end=', ')

# Cambiar valor de tupla
#

# Conversion de tupla a lista, y de lista a tupla
fruitsList = list(fruits)
fruitsList[0] = 'Pera'
fruits = tuple(fruitsList)
print('\n', fruits)

# Eliminar la tupla
del fruits
print(fruits)

