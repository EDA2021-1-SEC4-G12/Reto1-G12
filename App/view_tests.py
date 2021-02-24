
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

catalog = None

# Load data
catalog = initCatalog(args.type_list)
loadData(catalog)
print('Videos cargados: ' + str(lt.size(catalog['videos'])))

# Sort videos (TOCA HACER TODO ACA, DEPRONTO CON UN FOR)
sortedVideos = controller.sortVideos(catalog, int(args.sample_size), str(args.sort_type))
print('Ordenando con: ' + str(args.sort_type))
print('Para el top ' + str(args.sample_size) + ' elementos (videos), el tiempo (mseg) es: ' + str(sortedVideos[0]))


