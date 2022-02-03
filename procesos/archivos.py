# leerEscribirArchivo.py
import markdown

open("file.md", "x")
f = open("file.md", "w")
f.write("# LeerEscribirArchivo.py \n"
        "## Crear archivo markdown \n"
        "se usa la funcion `open` con el comando `x` \n"
        "## Escribir en archivo markdown\n"
        "se usa la funcion `open` con el comando `w`. Este comando reescribira todo el contenido del archivo, el cual es ninguno en este momento\n"
        "## Leer archivo markdown\n"
        "se usa la funcion `open` con el comando `r`. Se pueden obtener todos los datos escritos ejecutando `read` en el objeto File generado. \n"
        "> En este ejercicio, se lee el contenido escrito y se escribe en un archivo `html` con ayuda de la libreria `markdown`.")
f.close()
f = open('file.md', 'r')
text = f.read()
html = markdown.markdown(text)

f = open('web.html', 'w')
f.write(html)