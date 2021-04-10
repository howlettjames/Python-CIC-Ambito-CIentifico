def multiplicacion(a, b):
    if b == 1:
        return a
    else: 
        return a + multiplicacion(a, b - 1)

print("Multiplicacion Recursiva")
print(multiplicacion(7, 8))