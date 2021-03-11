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
import datetime
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

    catalog['videos'] = lt.newList(type_list
                                    ,cmpfunction=cmpvideoid)
    catalog['category_id'] = lt.newList(type_list
                                    ,cmpfunction=cmpcategoryid)

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
    id_ = newID(id['id'],id['name'])
    lt.addLast(catalog['category_id'], id_)


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
    id_ = {'name': '', 'id': ''}
    id_['name'] = name
    id_['id'] = id
    return id_


# Funciones de consulta

def getVideosByCategory(catalog, category):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    categories = catalog['category_id']
    vals_id = []
    names_id = []
    for elemt in categories['elements']:
        vals_id.append(elemt['name'])
        names_id.append(elemt['id'])
    dic_decode = dict(zip(names_id,vals_id))
    categoryVideos = lt.newList()
    for v_i in range(catalog['videos']['size']):
        video_i = dict(lt.getElement(catalog['videos'],v_i))
        if int(video_i['category_id']) == int(dic_decode[category]):
            lt.addLast(categoryVideos,video_i)

    return categoryVideos


def getVideosByCountry(catalog, country):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    countryVideos = lt.newList()
    for video in lt.iterator(catalog['videos']):
        video_country = video['country']
        if video_country == country:
            lt.addLast(countryVideos,video) 
    return countryVideos


def getVideosByTags(catalog, tag):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    tagsVideos = lt.newList()
    for v_i in range(catalog['videos']['size']):
        video_i = lt.getElement(catalog['videos'],v_i)
        tags_i = video_i['tags'].split('"|"')
        if tag in tags_i:
            lt.addLast(tagsVideos,video_i)
        
    return tagsVideos


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

def cmpcategoryid(id,category):
    return (id == category['name'])


def cmpVideosByViews(video1,video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) < float(video2['views']))

def cmpVideosByLikes(video1,video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['likes']) < float(video2['likes']))

def cmpVideosByTime(video1,video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    time1_b = datetime.datetime.strptime(video1['trending_date'], '%y.%d.%m')
    time1_a = datetime.datetime.strptime(video1['publish_time'], '%Y-%m-%d')
    days1 = time1_b-time1_a
    time2_b = datetime.datetime.strptime(video2['trending_date'], '%y.%d.%m')
    time2_a = datetime.datetime.strptime(video2['publish_time'], '%Y-%m-%d')
    days2 = time2_b-time2_a
    return (days1.days) < (days2.days)

# Funciones de ordenamiento

def sortVideos(catalog, size, sort_type):
    sub_list = lt.subList(catalog, 0, size)
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

def sortVideosLikes(catalog, size, sort_type):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = None
    if sort_type == 'selection':
        sorted_list = selectionsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'insertion':
        sorted_list = insertionsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'shell':
        sorted_list = shellsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'merge':
        sorted_list = mergesort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'quick':
        sorted_list = quicksort.sort(sub_list, cmpVideosByTime)
    else:
        print('Invalid sorting algorithm, try selection, insertion or shell')
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def sortVideosTime(catalog, size, sort_type):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = None
    if sort_type == 'selection':
        sorted_list = selectionsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'insertion':
        sorted_list = insertionsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'shell':
        sorted_list = shellsort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'merge':
        sorted_list = mergesort.sort(sub_list, cmpVideosByTime)
    elif sort_type == 'quick':
        sorted_list = quicksort.sort(sub_list, cmpVideosByTime)
    else:
        print('Invalid sorting algorithm, try selection, insertion or shell')
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list