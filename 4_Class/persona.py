class Persona:
    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError('Se esperaba una cadena')
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int):
            self.__edad = edad
        else:
            raise TypeError('Se esperaba un entero')

    def __str__(self):
        return f"\nCadena de objeto\nNombre: {self.nombre}\nEdad: {self.edad}"

    def __repr__(self):
        return f"Persona ({self.nombre}, {self.edad})"

    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return False
        else:
            return self.nombre == otro.nombre and self.edad == otro.edad

    def __ne__(self, otro):
        return not self.__eq__(otro)

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def printInfo(self):
        informacion = f"\nNombre: {self.__nombre}\nEdad: {self.__edad}"
        print(informacion)