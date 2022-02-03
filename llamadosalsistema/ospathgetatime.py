import os
import time
#os.path.getatime(path) retorna el tiempo de la última modificación (por eso la 'a') al path, en segundos
#por lo tanto se convierte a fecha con la librería time
print(time.ctime(os.path.getatime(os.getcwd())))
