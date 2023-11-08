def fibonnacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonnacci(n - 1) + fibonnacci(n - 2)


objetivo = int(input('Ingrese un numero: \n'))
respuesta = fibonnacci(objetivo)
print(f'La cantidad de conejos hembra en el mes {objetivo} es {respuesta}')
