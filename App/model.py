"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort, insertionsort, shellsort, mergesort, quicksort
assert cf




"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(type_list='SINGLE_LINKED'):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    if type_list != 'SINGLE_LINKED' and type_list != 'ARRAY_LIST':
        print('Invalid type')

    catalog = {'videos':None,
               'category_id': None}

    catalog['videos'] = lt.newList(type_list,
                                    cmpfunction=cmpvideoid)
    catalog['category_id'] = lt.newList(type_list,
                                    cmpfunction=cmpcategoryid)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)


def addID(catalog, id):
    """compareratings
    Adiciona un tag a la lista de tags
    """
    lt.addLast(catalog['category_id'], id)

# Funciones para creacion de datos

def newChannel(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    channel = {'name': "", "videos": None,  "likes": 0}
    channel['name'] = name
    channel['videos'] = lt.newList('ARRAY_addChannelLIST')
    return channel


def newID(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    id = {'name': '', 'id': ''}
    id['name'] = name
    id['id'] = id
    return id

# Funciones de consulta

def getVideosByCategory(catalog, category):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    poscategory = lt.isPresent(catalog['category_id'], category)
    if poscategory > 0:
        category_ = lt.getElement(catalog['category_id'], poscategory)
        return category_
    return None

def getVideosByCountry(catalog, country):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    poscountry = lt.isPresent(catalog['country'], country)
    if poscountry > 0:
        country_ = lt.getElement(catalog['country'], poscountry)
        return country_
    return None

def getBestVideos(catalog, number):
    """
    Retorna los mejores videos
    """
    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpvideoid(video1,video2):
    if (video1.lower() in video2['video_id'].lower()):
        return 0
    return -1

def cmpcategoryid(id1,id2):
    if (id1.lower() in id2['id'].lower()):
        return 0
    return


def cmpVideosByViews(video1,video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento

def sortVideos(catalog, size, sort_type):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = None
    if sort_type == 'selection':
        sorted_list = selectionsort.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'insertion':
        sorted_list = insertionsort.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'shell':
        sorted_list = shellsort.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'merge':
        sorted_list = mergesort.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'quick':
        sorted_list = quicksort.sort(sub_list, cmpVideosByViews)
    else:
        print('Invalid sorting algorithm, try selection, insertion or shell')
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list