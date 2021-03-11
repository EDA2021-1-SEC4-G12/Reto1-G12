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
import datetime
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
    print("3- Consultar los Top videos por views, categoría y país")
    print("4- Consultar video más trending para país")
    print("5- Consultar video más trending para categoría")
    print("6- Consultar los Top videos por país con tags")
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


def printTop(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size:
        print("Los primeros ", sample, " videos ordenados son:")
        i=0
        while i < sample:
            videos = lt.getElement(ord_videos,i)
            print('Trending date: {} ||  Title: {} ||  Channel: {}  ||  Published: {}  ||  Views: {}  ||  Likes: {}  ||  Dislikes: {}'.format(videos['trending_date'],videos['title'],videos['channel_title'],
                                                       videos['publish_time'],videos['views'],videos['likes'],videos['dislikes']))
            i+=1
    return printResults


def printTopTrendingCountry(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size:
        i=0
        while i < sample:
            videos = lt.getElement(ord_videos,i)
            trending_days = datetime.datetime.strptime(videos['trending_date'], '%y.%d.%m') - datetime.datetime.strptime(videos['publish_time'], '%Y-%m-%d')
            print('Title: {} ||  Channel: {}  ||  Country: {}  ||  Trending days: {}'.format(videos['title'],videos['channel_title'],
                                                       videos['country'],trending_days.days))
            i+=1


def printTopTrendingCategory(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size:
        i=0
        while i < sample:
            videos = lt.getElement(ord_videos,i)
            trending_days = datetime.datetime.strptime(videos['trending_date'], '%y.%d.%m') - datetime.datetime.strptime(videos['publish_time'], '%Y-%m-%d')
            print('Title: {} ||  Channel: {}  ||  Category: {}  ||  Trending days: {}'.format(videos['title'],videos['channel_title'],
                                                       videos['category_id'],trending_days.days))
            i+=1


def printCategoryCountry(videos_selected, sample, category, country):
    size = lt.size(videos_selected)
    if size:
        print('Los mejores ' + str(sample) + ' para la categoría ' + category + ' en ' + country)
        i=0
        while i < sample:
            videos = lt.getElement(videos_selected,i)
            print('Trending date: {} ||  Title: {} ||  Channel: {}  ||  Published: {}  ||  Views: {}  ||  Likes: {}  ||  Dislikes: {}'.format(videos['trending_date'],videos['title'],videos['channel_title'],
                                                       videos['publish_time'],videos['views'],videos['likes'],videos['dislikes']))
            i+=1
    return printResults

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        input_type_list = 'ARRAY_LIST'
        print("Cargando información de los archivos ....")
        catalog = initCatalog(input_type_list)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            
    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        input_sort_type = 'merge'
        sortedVideos = controller.sortVideos(catalog, int(number), str(input_sort_type))
        #print('Para el top ' + str(number) + ' elementos (videos), el tiempo (mseg) es: ' + str(sortedVideos[0]))
        printTop(sortedVideos[1], int(number))

    elif int(inputs[0]) == 3:
        number = input("Buscando los TOP ?: ")
        category = input('Categoria: ')
        country = input('País: ')
        input_sort_type = 'merge'
        categoryVideos = controller.getVideosByCategory(catalog, category)
        countryVideos = controller.getVideosByCountry(categoryVideos, country)
        sortedVideos = controller.sortVideos(countryVideos, int(number), str(input_sort_type))
        printCategoryCountry(sortedVideos[1], number, category, country)

    elif int(inputs[0]) == 4:
        country = input('País: ')
        input_sort_type = 'merge'
        countryVideos = controller.getVideosByCountry(catalog, country)
        sortedVideosTime = controller.sortVideosTime(countryVideos, int(1), str(input_sort_type))
        printTopTrendingCountry(sortedVideosTime[1], int(number))

    elif int(inputs[0]) == 5:
        category = input('Categoria: ')
        input_sort_type = 'merge'
        categoryVideos = controller.getVideosByCategory(catalog, category)
        sortedVideosTime = controller.sortVideosTime(categoryVideos, int(1), str(input_sort_type))
        printTopTrendingCategory(sortedVideosTime[1], int(number))

    elif int(inputs[0]) == 6:
        country = input('País: ')
        tag = input('Tag: ')
        input_sort_type = 'merge'
        tagsVideos = controller.getVideosByTags(catalog, tag)
        sortedVideosLikes = controller.sortVideosLikes(categoryVideos, int(3), str(input_sort_type))


    else:
        sys.exit(0)
sys.exit(0)
