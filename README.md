# Analizador Lexico (Lexer)

## Descripción del Proyecto 

Este es proyecto tiene con finalidad crear un **analizador léxico** para un lenguaje de programación propio, a el cual hemos llamado **skyblue** 

# Documentación
Este lexer fue desarrollado en **Python 3** para ser ejecutado en consola.
Básicamente este lo que hace es analizar un archivo con extensión **.blur** que contiene el código escrito con las reglas de nuestro lenguaje de programación
### Estructura del programa
* Carpeta **ply/** : contiene la librería empleada para hacer el lexer.
* Carpeta **archivos/** : contiene los archivos **.blur** dónde están códigos .
* Carpeta **clases/** : como su nombre lo indica contiene las clases 

### Versiones
Existen tres tipos de lexer, cada uno tiene pequeños cambios pero la misma lógica

* Archivo **lexer.py** : es la versión principal, es la versión más completa por así decirlo 

* Archivo **lexer_lite.py** : la principal diferencia entre esta y la principal es que en esta los tipos de *Token* están más generalizados, por lo cual esta sería una versión más liviana ya que contienen menos líneas de código.

* Archivo **lexer_v1.0.py** : en esta versión no contamos con la barra de progreso (progressbar).

### Ejecución en consola
Para ejecutar cualquiera de estas versiones se debe indicar en la consola que use la una version superior a la 3 de *Python*.

Puedes utilizar el siguiente comando:
```
python3 lexer.py
```    

### Descarga
Puedes clonar el repositorio de **Github** con el comando:
```
git clone https://github.com/unimag-compilers/Lexer.git

```    
O puedes descargar todo el proyecto en un archivo zip en el siguiente link:
    
[Click Para Descargar Lexer.zip](https://github.com/unimag-compilers/Lexer/archive/master.zip)

## Autores
* **Samir Mejia** - *Desarrollador* - [samir04m en Github](https://github.com/samir04m)
* **Cristian Charris** - *Desarrollador* - [cristiancharris en Github](https://github.com/cristiancharris)

## Licencia
Licencia estándar para repositorios públicos de [**Github**](https://github.com)
