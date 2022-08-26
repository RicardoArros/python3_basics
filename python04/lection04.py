# Dict (key, value)

#
dictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(dictionary)

# Largo
print(len(dictionary))

# Acceder a un elemento (key)
print(dictionary['IDE'])

# Otra forma de recuperar un elemento
print(dictionary.get('OOP'))

# Modificando elementos
dictionary['IDE'] = 'ambiente de desarrollo integrado'
print(dictionary)

# Recorrer los elementos
for term, value in dictionary.items():
    print(term, value, end=' - ')

print('\n')

for term in dictionary.keys():
    print(term, end='\n')

for value in dictionary.values():
    print(value)

# Comprobar existencia de algún elemento
print('IDE' in dictionary)

# Agregar un elemento
dictionary['PK'] = 'Primary Key'
print(dictionary)

# Remover un elemento
dictionary.pop('IDE')
print(dictionary)

# Limpiar
dictionary.clear()
print(dictionary)

# Eliminar el diccionario
del dictionary
print(dictionary)
