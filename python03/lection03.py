# Lection 03

# Break
for letter in 'Holanda':
    if letter == 'a':
        print(f'Letra encontrada: {letter}')
        break
else:
    print('Fin ciclo for')


# Continue
for i in range(6):
    print(f'Valor: {i}')

for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')