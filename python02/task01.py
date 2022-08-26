# Task 01

#
number = int(input('Proporciona un valor entre 1 y 3: '))
numberText = ''

#
if number == 1:
    numberText = 'Numero 1'
elif number == 2:
    numberText = 'Numero 2'
elif number == 3:
    numberText = 'Numero 3'
else:
    numberText = 'Fuera del rango'

#
print(f'Numero seleccionado: {number}, {numberText} ')
