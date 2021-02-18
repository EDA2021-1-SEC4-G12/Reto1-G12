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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
               'trending_date': None,
               'title': None,
               'channel_title': None,
               'publish_time': None,
               'views': None,
               'likes': None,
               'dislikes': None}

    catalog['videos'] = lt.newList()
    catalog['trending_date'] = lt.newList()
    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList()
    catalog['publish_time'] = lt.newList()
    catalog['views'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareviews)
    catalog['likes'] = lt.newList()
    catalog['dislikes'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    trending_dates = video['trending_date'].split(",")
    titles = video['title'].split(",")
    channel_titles = video['channel_title'].split(",")
    publish_times = video['publish_time'].split(",")
    views = video['views'].split(",")
    likes = video['likes'].split(",")
    dislikes = video['dislikes'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for channel_title in channel_titles:
        addChannel(catalog, author.strip(), book)

def addChannel(catalog, channelname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channels = catalog['channel_title']
    poschannel = lt.isPresent(channels, channelname)
    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newChannel(channelname)
        lt.addLast(channels, channel)
    lt.addLast(author['books'], book)


def addID(catalog, id):
    """compareratings
    Adiciona un tag a la lista de tags
    """
    t = newID(id['name'], tagid['id'])
    lt.addLast(catalog['ids'], t)

# Funciones para creacion de datos

def newChannel(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    channel = {'name': "", "videos": None,  "likes": 0}
    channel['name'] = name
    channel['videos'] = lt.newList('ARRAY_LIST')
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

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def sortVideos(catalog):
    sa.sort(catalog['videos'], compareviews)