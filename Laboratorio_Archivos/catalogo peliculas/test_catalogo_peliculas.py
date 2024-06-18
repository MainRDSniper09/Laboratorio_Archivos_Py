from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas  # Importamos las dos librerias correspondientes

print('Bienvenido al catalogo de peliculas'.center(50,'+'))  # Hacemos mensaje de bienvenida al usuario
while True:  # Hacemos un while siempre True para que este siempre se muestre
    print('''
Ingrese alguna de las opciones disponibles:
1. Agregar una película al catálogo
2. Listar las películas
3. Eliminar archivo de películas
4. Salir del programa
''')
    opcion = int(input('Seleccione una opcion: '))  # Le pedimos al usuario que digite una de las opciones vistas

    if opcion == 1:  # En caso de que seleccione el numero 1
        cantidadP = int(input('Ingrese la cantidad de peliculas que queire ingresar: '))  # Se crea una variable la cual recible un numero entero, indicandole al usuario la cantidad de peliculas que quiere digitar
        for i in range(cantidadP):  # Iteramos la cantidad de peliculas que el usuario quiere digitar
            nombre_pelicula = input('Ingrese el nombre de la pelicula: ')  # Le pedimos que ingrese el nombre de la pelicula y la guarde en la variable nombre_pelicula
            pelicula = Pelicula(nombre_pelicula)  # Creamos un objeto Pelicula que recibe el parametro de 'nombre_pelicula' digitado por el usuario
            CatalogoPeliculas.agregar_pelicula(pelicula)  # Llamamos la funcion creada anteriormente para agregar las peliculas correspondientes y le pasamos como parametro la variable pelicula

    if opcion == 2:  # En caso tal de que sea seleccionado el numero 2
        CatalogoPeliculas.listar_peliculas()  # Simplemente mandamos a llamar el metodo 'listar_peliculas()'

    if opcion == 3:  # En caso de que sea seleccionada el numero 3
        CatalogoPeliculas.eliminar()  # Simplemente mandamos a llamar el metodo 'eliminar()'

    if opcion == 4:  # En caso de que sea seleccionado el numero 4
        print('Saliendo del programa')  # Se imprime el mensaje para que el usuario sepa
        exit()  # Se ejecuta el metodo 'exit()' para que finalice el programa



