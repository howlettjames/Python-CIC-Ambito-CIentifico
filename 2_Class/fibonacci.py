"""
Descripcion: Programa de la serie de fibonacci
Autor: Jaime Bastida

"""
def fibonacci(limite):
    """
    Descripcion: Funcion que hace la serie de Fibonacci
    """
    a = 0
    b = 1
    while(a < limite):
        print(a, end = " ")
        #nuevo = a + b        
        #a = b
        #b = nuevo
        a, b = b, a + b

    print()

limite = int(input("Ingresa el limite de la serie de Fibonacci: "))
fibonacci(limite)
