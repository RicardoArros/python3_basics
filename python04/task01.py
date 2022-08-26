# Task 01

# Sintaxis de range(inicio, fin, incremento)

# Exercise 1
print('Rango de 0 a 10 con numeros divisibles entre 3:')

for i in range(11):
    if i % 3 == 0:
        print(i)

# Exercise 2
print('Rango con valores de inicio = 2, y fin = 6')

myRange = range(2, 7)

for i in myRange:
    print(i)

# Exercise 3
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')

myRange = range(3, 11, 2)

for i in myRange:
    print(i)