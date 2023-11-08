def factorial(n):
    """Calcula el factorial de n.

    n int>0
    return n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


objetivo = int(input('Ingrese un numero: \n'))
respuesta = factorial(objetivo)
print(f'El factorial de {objetivo} es {respuesta}')
