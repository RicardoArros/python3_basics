# Task 04

#
qualification = float(input('Proporciona un valor entre 0 y 10: '))
message = None

#
if qualification >= 9 and qualification <= 10:
    message = 'A'
elif qualification >= 8 and qualification < 9:
    message = 'B'
elif qualification >= 7 and qualification < 8:
    message = 'C'
elif qualification >= 6 and qualification < 7:
    message = 'D'
elif qualification >= 0 and qualification < 6:
    message = 'F'
else:
    message = 'Valor incorrecto'

#
print(f'La calificacion es {message}')
