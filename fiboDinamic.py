import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    # Importante: El codigo abajo esta comentado, para usarlo hay que descomentarlo, 
    # hay que tener en cuenta que cuanto mayor el el numero la recursividad por si 
    # sola va a llevar mas tiempo resolverlo, ahi esta la diferencia con la dinamica.
    '''resultado = fibonacci_recursivo(n)
    print('Resulado Recursivo')
    print(resultado)'''
    resultado = fibonacci_dinamico(n)
    print('Resulado Dinamico')
    print(resultado)