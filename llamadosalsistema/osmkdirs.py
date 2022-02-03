import os
#os.makedirs(path) crea directorios recursivamente, es decir, directorios dentro directorios
newDirs = os.path.join("sistemas","operativos")
path = os.path.join(os.getcwd(),newDirs)
print(os.makedirs(path))
#resultado
#./sistemas/operativos