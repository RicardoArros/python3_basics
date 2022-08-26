# Task 03

# Calcular el area y el perimetro de un rectangulo
height = int(input("Proporciona el alto del rectangulo: "))
width = int(input("Proporciona el ancho del rectangulo: "))

print(f'Alto: {height}')
print(f'Ancho: {width}')

area = height * width
perimetro = (height + width) * 2

print(f'Area: {area}')
print(f'Perimetro: {perimetro}')
