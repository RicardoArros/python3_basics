# Lection 01

# Definir una lista de tipo str
names = ['Juan', 'Karla', 'Ricardo', 'Maria']

# Imprimir la lista names
print(names)

# Acceder a los elementos de una lista
print(names[0])

# Acceder a los elementos de una lista de manera inversa
print(names[-1])

# Imprimir solo un rango
print(names[0:2])

# Ir del inicio de la lista al índice (sin incluirlo)
print(names[:3])

# Ir desde el índice indicado hasta el final
print(names[1:])

# Cambiar de valor
names[3] = 'Ivone'
print(names)

# Iterar una lista
for name in names:
    print(name)
else:
    print('No existen más nombres en la lista')

# Preguntar el largo de la lista
print(len(names))

# Agregar un elemento
names.append('Lorenzo')
print(names)

# Insertar un elemento en un índice en específico
names.insert(1, 'Octavio')
print(names)

# Remover por valor de elemento
names.remove('Octavio')
print(names)

# Remover por último valor agregado
names.pop()
print(names)

# Remover por índice
del names[0]
print(names)

# Limpiar la lista
names.clear()
print(names)

# Borrar la lista por completo
del names
print(names)