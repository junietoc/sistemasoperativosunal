import os
#os.path.getsize(path) retorna el tamaño en bytes, del archivo indicado en el path 
path = os.path.join(os.getcwd(),"osjoin.py")
print(os.path.getsize(path))