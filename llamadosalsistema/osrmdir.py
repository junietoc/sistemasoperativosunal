import os
#os.rmdir elimina directorio indicado en el path, el directorio debe estar vacío de lo contrario produce error
path = os.path.join(os.getcwd(),"sistemas")
print(os.rmdir(path))