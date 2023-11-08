objetivo = int(input('Ingrese un entero: \n'))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1


print(f'La raiz cuadrada de {objetivo} es {respuesta}') if respuesta**2 == objetivo else print(
    f'{objetivo} no tiene una raiz cuadrada exacta')
