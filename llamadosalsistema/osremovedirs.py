import os
#os.removedirs elimina directorios recursivamente comenzando por el directorio hoja
#el cual es el ultimo indicado en el path y llendo hacia atrás eliminando directorios padres
#mientras estos estén vacíos
path = os.path.join(os.getcwd(),"sistemas\operativos")
print(os.removedirs(path))