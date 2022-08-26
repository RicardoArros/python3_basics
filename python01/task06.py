# Task 06

# and
value = int(input("Escribe el valor: "))

valueMin = 0
valueMax = 5

range = (value >= valueMin) and (value <= valueMax)

if range:
    print((f'El valor {value} está dentro del rango'))
else:
    print((f'El valor {value} está fuera del rango'))


# or
holidays = False
dayOff = False

if holidays or dayOff:
    print("Puede asistir al juego")
else:
    print("Tiene deberes por hacer")


# not
if not (holidays or dayOff):
    print("Tiene deberes por hacer")
else:
    print("Puede asistir al juego")

