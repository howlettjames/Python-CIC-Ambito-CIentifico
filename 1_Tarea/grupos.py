nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (F o H): ")

grupo = ""
if(genero == 'F' and nombre.lower() < "m") or (genero == 'H' and nombre.lower() > 'n'):
    grupo = "G1"
else:
    grupo = "G2"

print(f'Tu grupo es {grupo}')