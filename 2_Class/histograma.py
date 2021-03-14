"""
Descripcion: Programa que imprime el histograma de frecuencias de un numero determinado de
             series de datos.
Autor: Jaime Bastida
"""

num_series = int(input("Ingrese el numero de series a graficar: "))

datos = {}
for x in range(num_series):
    nombre_serie = input("Ingresa el nombre de la serie: ")
    frecuencia = int(input("Ingresa su frecuencia: "))
    datos[nombre_serie] = frecuencia

llaves = datos.keys()
for llave in llaves:
    frecuencia = datos[llave]
    histograma = llave + " : " + ("*" * frecuencia)
    print(histograma)