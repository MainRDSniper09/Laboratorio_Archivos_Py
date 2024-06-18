from dominio.Pelicula import Pelicula  # Se importa la clase Pelicula


class CatalogoPeliculas(Pelicula):
    ruta_archivo = '/home/mainrdsniper09/Documentos/ArchivosImportantes-main/Cursos/Python/Archivos/Laboratorio_Archivos/catalogo peliculas/catalogo.txt'  # Se crea la variable donde se almacenara la ruta del archivo

    @staticmethod
    def agregar_pelicula(pelicula):  # Se crea el metodo estatico de 'agregar_pelicula' en donde como parametro recibe 'pelicula'
        with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8') as archivo:  # creamos la funcion para abrir el archivo y que este anexe las peliculas correspondientes, esto se lo asignamos a el objeto archivo
            archivo.write(f'{pelicula.nombre}\n')  # Hacemos uso del metodo 'write()' en donde recibe el parametro de 'pelicula.nombre' para escribir en nuestro archivo

    @staticmethod
    def listar_peliculas():  # Se crea el metodo estatico 'listar_peliculas'
        try:  # Creamos un bloque try and exception
            with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8') as archivo:  # Hacemos uso nuevamente de with, lo guardamos en el objeto archivo
                print('Catalogo de Peliculas:')  # Imprimimos un aviso en donde dice que corresponde al catalogo de peliculas
                print(archivo.read())  # Imprimimos la funcion 'read()' en donde lee todo el archivo y lo imprime por consola
        except Exception as e:  # Hacemos uso de las excepciones para asegurarnos de cualquier error
            print(f'El archivo no existe o no se ha podido encontrar {e}')  # Imprimimos el mensaje de error en caso tal de que no encuentre el archivo correspondiente

    @staticmethod
    def eliminar():  # Se crea el metodo estatico de 'eliminar'
        with open(CatalogoPeliculas.ruta_archivo, 'w', encoding='utf8') as archivo:  # Hacemos uso nuevamente de with en donde le asignamos nuevamente al objeto archivo
            pass  # Hacemos que pase de la operacion ya que lo tenemos en modo 'w' o modo escritura, al no escribir nada, entonces esto lo que hara es borrar todo el catalogo de peliculas
        print('Catalogo eliminado')  # Mandamos a imprimir un mensaje al usuario para que sepa que ya se elimino todo

