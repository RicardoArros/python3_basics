# Task 02

#
month = int(input('Proporciona mes del año (1-12)'))
season = None

#
if month == 1 or month == 2 or month == 12:
    season = 'Verano'
elif month == 3 or month == 4 or month == 5:
    season = 'Otoño'
elif month == 6 or month == 7 or month == 8:
    season = 'Invierno'
elif month == 9 or month == 10 or month == 11:
    season = 'Primavera'
else:
    season = 'Mes incorrecto'

print(f'Para el mes {month} la estacion es: {season}')

