
from typing import Pattern
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
import argparse
parser = argparse.ArgumentParser(description='Testing sorts')

parser.add_argument('--type_list', default='SINGLE_LINKED', type=str)

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
    
# Load data
catalog = initCatalog(args.type_list)
loadData(catalog)
print('Videos cargados: ' + str(lt.size(catalog['videos'])) + ' || ' + str(args.type_list))

# Sort videos

sort_types = ['selection','insertion','shell', 'merge', 'quick']
sample_size = [1000,2000,4000,8000,16000,32000]

for sort_ in sort_types:
    for sample_size_ in sample_size:
        sortedVideos = controller.sortVideos(catalog, sample_size_, sort_)
        print('Ordenando con: ' + sort_)
        print('Para el top ' + str(sample_size_) + ' elementos (videos), el tiempo (mseg) es: ' + str(sortedVideos[0]))