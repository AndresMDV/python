objetivo = int(input('Ingrese un numero: \n'))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso


print('no se encontro la raiz cuadrada del objetivo') if abs(respuesta**2 - objetivo) >= epsilon else print(
    f'la raiz cuadrdad de {objetivo} es {respuesta}')
