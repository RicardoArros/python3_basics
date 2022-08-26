# Set

#
planets = {'Marte', 'Jupiter', 'Venus'}
print(planets)

# length
print(len(planets))

# Check if element exist
print('Marte' in planets)

# Agregar un elemento
planets.add('Tierra')
print(planets)

# No se pueden duplicar elementos
planets.add('Tierra')
print(planets)

# Eliminar elemento posiblemente arrojando un error
planets.remove('Tierra')
print(planets)

# Eliminar elemento sin arrojar error
planets.discard('Venus')
print(planets)

# Limpiar Set
planets.clear()
print(planets)

# Eliminar el Set
del planets
print(planets)
