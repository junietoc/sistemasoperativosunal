import os
from colorama import Fore
#os.walk realiza un recorrido por los archivos y directorios del path indicado y retorna
#el directorio raiz, y lista de directorios y archivos
os.chdir("C:\\Users\\ASUS\\Documents\\Universidad\\Semestre 2")
print(os.getcwd())
for root, dirs, files in os.walk(".", topdown=False):
    print(Fore.YELLOW + "directorio: " + root)
    for name in files:
        print(Fore.WHITE + os.path.join(root, name))
    for name in dirs:
        print(Fore.WHITE + os.path.join(root, name))