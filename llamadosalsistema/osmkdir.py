import os
# la función "os.makdir()" crea un directorio en el path indicado, el path debe incluir el nombre del nuevo directorio

path = os.path.join(os.getcwd(),"nuevoDirectorio")
print(os.mkdir(path))