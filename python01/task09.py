# Task 09

#
print('Proporcione los siguientes datos del libro: ')

#
name = input('Proporcione el nombre del libro: ')
id = int(input('Proporcione el id del libro: '))
price = float(input('Proporcione el precio del libro: '))
isShippingFree = (input('Envío gratuito? (True/False): '))

#
if isShippingFree == 'True':
    isShippingFree = True
elif isShippingFree == 'False':
    isShippingFree = False
else:
    isShippingFree = 'Valor incorrecto, debe escribir True/False'

#
print(f'''
    Nombre: {name}
    id: {id}
    Precio: {price}
    Envio gratuito?: {isShippingFree}
''')
