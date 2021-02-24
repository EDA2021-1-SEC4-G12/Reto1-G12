
from typing import Pattern
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
import argparse
parser = argparse.ArgumentParser(description='Testing sorts')

parser.add_argument('--type_list', default='SINGLE_LINKED', type=str)
parser.add_argument('--sample_size', default=10, type=int)
parser.add_argument('--sort_type', default='selection', type=str)

args = parser.parse_args()


# def printMenu():
#     print("Bienvenido")
#     print("1- Cargar información en el catálogo")
#     print("2- Consultar los Top videos por views")
#     print("3- Consultar los videos de un canal")
#     print("4- Consultar videos por género")
#     print("0. Salir")
    
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

# def printResults(ord_videos, sample=10):
#     size = lt.size(ord_videos)
#     if size > sample:
#         print("Los primeros ", sample, " videos ordenados son:")
#         i=0
#         while i <= sample:
#             videos = lt.getElement(ord_videos,i)
#             print('Trending date: ' + videos['trending_date'] + ' Title: ' + videos['title']
#                   + ' Channel: ' + videos['channel_title'] + ' Views: ' + videos['views'])
#             i+=1

catalog = None

# Load data
catalog = initCatalog(args.type_list)
loadData(catalog)
print('Videos cargados: ' + str(lt.size(catalog['videos'])))

# Sort videos (TOCA HACER TODO ACA, DEPRONTO CON UN FOR)
sortedVideos = controller.sortVideos(catalog, int(args.sample_size), str(args.sort_type))
print('Ordenando con: ' + str(args.sort_type))
print('Para el top ' + str(args.sample_size) + ' elementos (videos), el tiempo (mseg) es: ' + str(sortedVideos[0]))


