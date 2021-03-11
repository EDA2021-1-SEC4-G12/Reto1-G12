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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


# Inicialización del Catálogo de libros
def initCatalog(type_list):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(type_list)
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadIDs(catalog)

def loadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-10pct.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadIDs(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    idsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(idsfile, encoding='utf-8'))
    for id in input_file:
        model.addID(catalog, id)

# Funciones de ordenamiento

def sortVideos(catalog, size, sort_type):
    """
    Ordena los videos por views
    """
    return model.sortVideos(catalog, size, sort_type)

def sortVideosTime(catalog, size, sort_type):
    """
    Ordena los videos por views
    """
    return model.sortVideosTime(catalog, size, sort_type)

def sortVideosLikes(catalog, size, sort_type):
    """
    Ordena los videos por views
    """
    return model.sortVideosLikes(catalog, size, sort_type)

# Funciones de consulta sobre el catálogo

def getVideosByCategory(catalog, category):
    """
    Retrona los videos de una categoria
    """
    categoryVids = model.getVideosByCategory(catalog, category)
    return categoryVids


def getVideosByCountry(catalog, country):
    """
    Retrona los videos de un pais trending
    """
    countryVids = model.getVideosByCountry(catalog, country)
    return countryVids

def getVideosByTags(catalog, tag):
    """
    Retrona los videos de un pais trending
    """
    tagsVids = model.getVideosByTags(catalog, tag)
    return tagsVids

def getVideosByCountryCat (catalog, country, category):

    count = model.getVideosByCatCoun (catalog, country, category)
    return count


def printResult (catalog, numbers):
    lista = []
    i = 0
    while i <=numbers :
        elemento = lt.getElement(catalog, i)
        lista.append(elemento)
        i += 1
    print(lista)

# def getBestVideos(catalog, number):
#     """
#     Retorna los mejores videos
#     """
#     bestvideos = model.getBestVideos(catalog, number)
#     return bestvideos