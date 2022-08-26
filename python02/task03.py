# Task 03

#
age = int(input('Proporciona tu edad: '))
message = None

#
if age >= 0 and age < 10:
    message = 'La infancia es increíble...'
elif age >= 10 and age < 20:
    message = 'Muchos cambios y mucho estudio...'
elif age >= 20 and age < 30:
    message = 'Amor y comienza el trabajo...'
else:
    message = 'Etapa de vida no reconocida'

#
print(f'Tu edad es: {age}, {message}')
