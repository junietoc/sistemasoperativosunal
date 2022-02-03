import os
#os.path.isfile retorna booleano indicando si el archivo existe en el path indicado
path = os.path.join(os.getcwd(),"ospathisfile.py")

print(os.path.isfile(path))