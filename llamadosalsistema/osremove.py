import os
#os.remove elimina el archivo indicado en el path
path = os.path.join(os.getcwd(), "file.txt")
print(os.remove(path))