import os
import time
#os.path.getmtime(path) retorna el tiempo del último acceso (por eso la 'm') al path, en segundos
#por lo tanto se convierte a fecha con la librería time
print(time.ctime(os.path.getmtime(os.getcwd())))