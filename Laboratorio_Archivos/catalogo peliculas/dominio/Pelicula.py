class Pelicula:  # Se crea clase Pelicula
    def __init__(self, nombre):  # Se crea el atributo nombre
        self.__nombre = nombre

    @property
    def nombre(self):  # Get atributo nombre
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):  # Set atributo nombre
        self.__nombre = nombre

    def __str__(self):  # Metodo __str__ para imprimir los datos correspondientes
        return f'Nombre de pelicula: {self.nombre}'

