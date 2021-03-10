"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top videos por views")
    print("3- Consultar los videos de un canal")
    print("5- Consultar videos por género")
    print("0. Salir")
    
def initCatalog(input_type_list):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(input_type_list)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


# def printAuthorData(author):
#     if author:
#         print('Autor encontrado: ' + author['name'])
#         print('Promedio: ' + str(author['average_rating']))
#         print('Total de libros: ' + str(lt.size(author['books'])))
#         for book in lt.iterator(author['books']):
#             print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
#     else:
#         print('No se encontro el autor')1


# def printBestVideos(videos):
#     size = lt.size(videos)
#     if size:
#         print(' Estos son los mejores videos: ')
#         for videos in lt.iterator(videos):
#             print('Titulo: ' + videos['title'] + '  ISBN: ' +
#                   video['isbn'] + ' Rating: ' + video['average_rating'])
#     else:
#         print('No se encontraron videos')1

def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i=0
        while i <= sample:
            videos = lt.getElement(ord_videos,i)
            print('Trending date: ' + videos['trending_date'] + ' Title: ' + videos['title']
                  + ' Channel: ' + videos['channel_title'] + ' Views: ' + videos['views'])
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #input_type_list = input('Tipo de list (ARRAY_LIST o SINGLE_LINKED) \n')
        input_type_list = 'ARRAY_LIST'
        print("Cargando información de los archivos ....")
        catalog = initCatalog(input_type_list)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            
    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        #input_sort_type = input('Tipo de algoritmo de ordenamiento iterativo (selection, insertion o shell) : ')
        input_sort_type = 'merge'
        sortedVideos = controller.sortVideos(catalog, int(number), str(input_sort_type))
        print('Para el top ' + str(number) + ' elementos (videos), el tiempo (mseg) es: ' + str(sortedVideos[0]))
        prin

    elif int(inputs[0]) == 3:
        channel_title = input("Nombre del pais a buscar: ")
        author = controller.getVideosByCountry(catalog, channel_title)
        printCountryData(author)

    elif int(inputs[0]) == 4:
        category = input("Etiqueta a buscar: ")
        book_count = controller.getVideosByCategory(catalog, category)
        print('Se encontraron: ', book_count, ' videos')

    else:
        sys.exit(0)
sys.exit(0)
