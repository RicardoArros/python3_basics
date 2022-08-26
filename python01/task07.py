# Task 07

# 1V
age = int(input('Introduce tu edad: '))

twenties = age >= 20 and age < 30
print(twenties)

thirties = age >= 30 and age < 40
print(thirties)

if twenties or thirties:
    print('Dentro de rango (20\'s) o (30\'s)')

    if twenties:
        print('Dentro de los 20\'s')
    elif thirties:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")


# 2V
age = int(input('Introduce tu edad: '))

if (age >= 20 and age < 30) or (age >= 30 and age < 40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print("No está dentro de los 20's ni 30's")


# 3V
age = int(input('Introduce tu edad: '))

if (20 <= age < 30) or (30 <= age < 40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print("No está dentro de los 20's ni 30's")

