import pandas as pd

#info de las 5 funciones de la librería os
funcion1 = ['os.name','Retorna el nombre del sistema operativo: posix, java, nt (windows)']
funcion2 = ['os.listdir', 'Retorna todas las entradas en el path indicado, tanto archivos como directorios']
funcion3 = ['os.mkdir', 'Crea un directorio en el path indicado, el path debe incluir el nombre del nuevo directorio']
funcion4 = ['os.join', 'Concatena dos cadenas retornando un path']
funcion5 = ['os.walk', 'Un recorrido por los archivos y directorios del path indicado y retorna el directorio raiz, y lista de directorios y archivos']
funciones = [funcion1,funcion2,funcion3,funcion4,funcion5]
#se crea el archivo de texto
open("funcionesOS.txt", "x")
#se escribe la info de las funciones en el archivo de texto
f = open("funcionesOS.txt", "w")
f.write("FuncionesOS  \n")
for funcion in funciones:
    f.write(funcion[0] + ": " + funcion[1] + "\n")


#se crea el archivo excel fu
file = pd.ExcelWriter('FuncionesOS.xlsx', engine='xlsxwriter')
#se escribe la info de las funciones en el archivo de excel
df = pd.DataFrame([funcion1,funcion2,funcion3,funcion4,funcion5],columns=['Función', 'Descripción'])
df.to_excel('FuncionesOS.xlsx')