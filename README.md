 
# Python Profesional

###  Profesor Facundo García Martoni 
### plataforma [Platzi](https://platzi.com/clases/2255-python-intermedio/)

## Organiza los archivos de tus proyectos
📁Un  **módulo**  es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar.

🗄 Un paquete es un conjunto de módulos. Siempre posee el archivo  **`__init__.py`**.  
Una ejemplo de organizar los archivos de 🐍Python es de la siguiente manera.

![paquettes.png](https://static.platzi.com/media/user_upload/paquettes-5a4095f3-0811-4e56-8f06-296b42b2e497.jpg)

### paquetes
un paquete es una carpeta que contiene módulos.
siempre posee el archivo .__init__.py


### Nota
Si están usando WSL o una terminal Unix, pueden instalar con  `sudo apt-get install tree`  para ver un árbol de sus carpetas.  
Luego puedo ingresar a la carpeta de mi proyecto y ejecutar el comando  `tree`.

Se vería algo así:

![](https://i.imgur.com/qCVtw4H.png)

Yo pongo  `tree -I venv`  para ignorar la carpeta venv que esta llena de cosas. Si no lo pongo verás todos los directorios de tu proyecto.

![](https://i.imgur.com/H9wQKS3.png)

## ¿Qué son los tipados?

Mini resumen:

**Estático**  →→ Detectan los errores en tiempo de compilación. No se ejecuta hasta corregir. Por ej,  _Java_

**Dinámico**  →→ Detectan el error en tiempo de ejecución. Nos dice el error cuando llega a la línea del código. Por ej,  _Python_

**Strong**  →→ Más severidad con los tipos de datos. Sumar un número + una letra arrojará error.

**Weak**  →→ Menos severidad con los tipos de datos. Si quiero sumar número y letra, las concatenaría como strings. Castea tipos de datos automáticamente. Por ej,  _PHP_
