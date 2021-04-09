'''
  @author: Jaime Bastida
  @description: Programa que presenta datos climatológicos
                generales para una ubicación geográfica
                definida por latitud y longitud.
'''
import requests

class LocalidadClima:
    def __init__(self, nombre, pais, temperatura, t_minima, t_maxima, humedad, presion, latitud, longitud):
        self.nombre = nombre
        self.pais = pais
        self.temperatura = temperatura
        self.t_minima = t_minima
        self.t_maxima = t_maxima
        self.humedad = humedad
        self.presion = presion
        self.latitud = latitud
        self.longitud = longitud

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError('Expected string')
        else:
            self.__nombre = nombre
    
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        if not isinstance(pais, str):
            raise TypeError('Expected string')
        else:
            self.__pais = pais

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if not isinstance(temperatura, float):
            raise TypeError('Expected float')
        else:
            self.__temperatura = temperatura

    @property
    def t_minima(self):
        return self.__t_minima

    @t_minima.setter
    def t_minima(self, t_minima):
        if not isinstance(t_minima, float):
            raise TypeError('Expected float')
        else:
            self.__t_minima = t_minima

    @property
    def t_maxima(self):
        return self.__t_maxima

    @t_maxima.setter
    def t_maxima(self, t_maxima):
        if not isinstance(t_maxima, float):
            raise TypeError('Expected float')
        else:
            self.__t_maxima = t_maxima

    @property
    def humedad(self):
        return self.__humedad

    @humedad.setter
    def humedad(self, humedad):
        if not isinstance(humedad, int):
            raise TypeError('Expected integer')
        else:
            self.__humedad = humedad
    
    @property
    def presion(self):
        return self.__presion

    @presion.setter
    def presion(self, presion):
        if not isinstance(presion, int):
            raise TypeError('Expected integer')
        else:
            self.__presion = presion
    
    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, longitud):
        if not isinstance(longitud, float):
            raise TypeError('Expected float')
        else:
            self.__longitud = longitud

    @property
    def latitud(self):
        return self.__latitud

    @latitud.setter
    def latitud(self, latitud):
        if not isinstance(latitud, float):
            raise TypeError('Expected float')
        else:
            self.__latitud = latitud
        
    @staticmethod
    def cambiaCentigrados(g_kelvin):
        if not isinstance(g_kelvin, float):
            raise TypeError('Expected float')
        else:
            return g_kelvin - 273.15

    def imprimeInformacion(self):
        print(f"Datos climatologicos generales para {self.nombre}")
        print(f"País: {self.pais}")
        print(f"Temperatura actual: {LocalidadClima.cambiaCentigrados(self.temperatura)}")
        print(f"Temperatura mínima: {LocalidadClima.cambiaCentigrados(self.t_minima)}")
        print(f"Temperatura máxima: {LocalidadClima.cambiaCentigrados(self.t_maxima)}")
        print(f"Humedad relativa: {self.humedad}")
        print(f"Presión atmosférica: {self.presion}")
        print(f"Coordenadas de la muestra: ({self.latitud}, {self.longitud})")

class GestorClima:
    api_key = "c751c6d8002c04b266d0b8706c8b2f72"
    url_base = 'http://api.openweathermap.org/data/2.5/weather?'

    def __init__(self):
        self.url_completa = self.url_base + 'lat={}&lon={}&appid=' + self.api_key    
    
    @property
    def url_completa(self):
        return self.__url_completa
    
    @url_completa.setter
    def url_completa(self, url_completa):
        if not isinstance(url_completa, str):
            raise TypeError('Expected stirng')
        else:
            self.__url_completa = url_completa

    def consultaCoordenadas(self, latitud = 21.126763, longitud = -86.819574):
        if not isinstance(latitud, float):
            raise TypeError('Expected float')
        elif not isinstance(longitud, float):
            raise TypeError('Expected float')
        else:        
            url_formato = self.url_completa.format(latitud, longitud)
            respuesta = requests.get(url_formato)
            dictRespuesta = respuesta.json()

            if(dictRespuesta['cod'] == '401'):
                print(dictRespuesta['message'])
                return None
            elif(dictRespuesta['cod'] != '404'):
                nombre_ciudad = dictRespuesta['name']
                dictInfPrincipal = dictRespuesta['main']
                temp_actual = dictInfPrincipal['temp']
                minima = dictInfPrincipal['temp_min']
                maxima = dictInfPrincipal['temp_max']
                presion_actual = dictInfPrincipal['pressure']
                humedad = dictInfPrincipal['humidity']
                clima = dictRespuesta['weather']
                weather_description = clima[0]['description']
                sys_doc = dictRespuesta['sys']
                pais = ''
                if 'country' in sys_doc:
                    pais = sys_doc['country']
                coordenadas = dictRespuesta['coord']
                lat = coordenadas['lat']
                lon = coordenadas['lon']
                return LocalidadClima(nombre_ciudad, pais, temp_actual, minima, maxima, humedad, presion_actual, lat, lon)
            else:
                return None
        
def main():
    present = '''
    =================================================
    === Programa que presenta datos climatológicos ==
    === generales para una ubicación geográfica =====
    === definida por latitud y longitud =============
    '''
    print(present)
    latitud = float(input('Proporcione una latitud: '))
    longitud = float(input('Proporcione una longitud: '))

    gestor = GestorClima()
    localidad = gestor.consultaCoordenadas(latitud, longitud)
    if type(localidad) != None:
        localidad.imprimeInformacion()

if __name__ == '__main__':
    main()