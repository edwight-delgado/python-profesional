 
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


## Tipado estático en Python


[Documentación oficial del tipado estático en Python](https://docs.python.org/3/library/typing.html)

El tipado estático nos hará evitar errores de tipado antes de que el programa se ejecute.

```python
a: int = 5
print(a) # 5

b: str = 'Hola'
print(b) # Hola

c: bool = True
print(c) # True

```

Esta sintaxís está disponible desde la versión 3.6 de Python.

```python
def suma(a: int, b: int) -> int:
  return a + b

print(suma(1,2)) # 3

```

```python
def suma(a: int, b: int) -> int:
  return a + b

print(suma('1','2')) # 12 😅

```

Usando tipado en estructuras de datos. Desde la versión 3.6 debemos importar librerias.

```python
from typing import Dict, List

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
  'argentina': 1,
  'mexico': 34,
  'colombia': 45,
}

countries: List[Dict[str,str]] = [
  {
    'name': 'Argentina',
    'people': '450000', # Cuatrocientos cincuenta mil
  },
  {
    'name': 'México',
    'people': '90000000', # Noventa millones
  },
  {
    'name': 'Colombia',
    'people': '99999999999', #novecientos noventa y nueve mil millones novecientos mil novecientos noventa y nueve
  }
]

```

```python
from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)

```

```python
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

#Una variable que es de tipo CoordinatesType 🤯
coordinates: CoordinatesType = [
  {
    'coord1': (1,2),
    'coord2': (3,5),
  },
  {
    'coord1': (0,1),
    'coord2': (2,5),
  },
]

```

Ventajas de esto:  _claridad del código_.

## Practicando el tipado estático
#### Modulo `mypy`

El modulo  **mypy**  se complementa con el modulo  **typing**  ya que permitirá mostrar los errores de tipado débil en Python.

    pip install mypy

Para revisar si algún archivo contiene errores de tipado ejecutamos en la línea de comandos lo siguiente:

```
mypy archivo.py --check-untyped-defs

```

Como resultado nos mostrará si existe algún error de compatibilidad de tipos.

## Scope: alcance de las variables



### Resumen

El scope es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso.  **Regla de oro:**

> _una variable solo esta disponible dentro de la region donde fue creada_

#### Local Scope

Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

#### Global Scope

Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.  

![Untitled.png](https://static.platzi.com/media/user_upload/Untitled-5d8878b2-048d-4017-a0de-a582e3f494d5.jpg)

Para visualizar el ámbito local y global de las variables:  

![scope.jpg](https://static.platzi.com/media/user_upload/scope-e9e77d30-f90a-4a93-b288-5c20b361d2a2.jpg)


## Closures


<h5>Nested Functions - Funciones anidadas</h5>

```python
def main():
  a = 1

  def nested():
    print(a)

  nested() # 1

main()

```

----------

closure:

```python
def main():
  a = 1

  def nested():
    print(a)

  return nested

my_func = main()
my_func() # 1

```

Quiere decir que una variable que está en un scope superior, es recordada por una función de scope inferior.

----------

```python
def main():
  a = 1

  def nested():
    print(a)

  return nested

my_func = main()
my_func() # 1

del(main) # borramos la función

my_func() # 1 🤯 debido a la nested function

```

Reglas para encontrar un closure:

-   Debemos tener una nested function.
-   La nested function debe referenciar un valor de un scope superior.
-   La función que envuelve a la nested function debe retornarla también.

```python
def make_multiplier(x):

  def multiplier(n):
    return x * n

  return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # => 10 * 3 = 30
print(times4(5)) # => 4 * 5 = 20
print(times10(times4(2))) # => 4 * 2 * 10 = 80

```

¿Dónde aparecen los closures?

1.  Clase con solo 1 método
2.  Cuando trabajamos con decoradores


## Programando closures
	def make_repeater_of(n):
		def repeater(string):
			assert type(string) == str,"solo puedes usar string"
			return string * n

		return repeater


	def main():
		repeat_5 = make_repeater_of(5)
		print(repeat_5('hola'))

	if __name__ == '__main__':
		main()

## Decoradores
Función que recibe como parametro otra función, le añade nuevas funcionalidades y retorna una función diferente.

Una función que le añade super poderes a otra función.

Ejemplo:

```python
def decorador(func):
	def envoltura():
		print("Esto se añade a mi función original")
		func()
	return envoltura

def saludo():
	print("Hola")

saludo() # output: Hola

saludo = decorador(saludo)
saludo = 
# output: 
# Esto se añade a mi función original
# Hola

```

De forma más estetica:

```python
def decorador(func):
	def envoltura():
		print("Esto se añade a mi función original")
		func()
	return envoltura

@decorador
def saludo()
	print("Hola")

saludo()
# output: 
# Esto se añade a mi función original
# Hola
```

Otro ejemplo:

```python
def mayusculas(func):
	def envoltura(texto):
		return func(texto).upper()
	return envoltura

@mayusculas
def mensaje(nombre):
	return f'{nombre}, recibiste un mensaje'

print(mensaje('Felipe'))

#output
FELIPE, RECIBISTE UN MENSAJE
```
## Programando decoradores
	from datetime import datetime

	def execution_time(func):
	    def wrapper(*args, **kwargs):
	        initial_time = datetime.now()
	        func(*args, **kwargs)
	        final_time = datetime.now()
	        time_elapsed = final_time - initial_time
	        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
	    return wrapper
	    
	@execution_time
	def random_func():
	    for _ in range(1, 10000000):
	        pass

	random_func()

## Iteradores
### Estructuras de datos avanzadas

#### Iteradores

Antes de entender qué son los iteradores, primero debemos entender a los iterables.

Son todos aquellos objetos que podemos recorrer en un ciclo. Son aquellas estructuras de datos divisibles en elementos únicos que yo puedo recorrer en un ciclo.

Pero en Python las cosas no son así. Los iterables se convierten en iteradores.

Ejemplo:

```python
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada

```

----------

```python
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

while True: #ciclo infinito
  try:
    element = next(my_iter)
    print(element)
  except StopIteration:
    break

```

**Momento impactante:**  El ciclo “for” dentro de Python, no existe. Es un while con StopIteration. 🤯🤯🤯

```python
my_list = [1,2,3,4,5]

for element in my_list:
  print(element)

```

----------

`evenNumbers.py`:

```python
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): #self hace referencia al objeto futuro que voy a crear con esta clase
    self.max = max


  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 #Primer número par
    #* Convertir un iterable en un iterador
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration

```

Ventajas de usar iteradores:

1.  Nos ahorra recursos.
2.  Ocupan poca memoria.


## Sucesion de fibonacci


```
from time import sleep
class FiboIter():

    def __init__(self, max_number:int):
        self.max_number = max_number
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            
            if self.aux >= self.max_number:
                raise StopIteration
            
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        


if __name__ == "__main__":
    for element in FiboIter(39):
        print(element)
        sleep(0.1)

```

## Generadores


Los generadores son azúcar sintáctica para los Iteradores. Son básicamente funciones que guardan un estado, a diferencia de los iteradores, que son clases.

Ejemplo:

```python
def my_gen():
	"""Un ejemplo de generadores"""
	print("Hello world")
	n = 0
	yield n

	print("Hello heaven")
	n = 1
	yield n

	print("Hello hell")
	n = 2
	yield n

a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) StopIteration

```

Yield es lo mismo que return, con la diferencia de que yield, en lugar de terminar la función solo pausa la función hasta donde estaba ese yield. Es decir, que si después se vuelve a llamar a la función no va a comenzar desde el principio, sino desde donde se quedó el último yield.

----------

#### Generator expressions

Son lo mismo que un list o dictionary comprehension pero para un generador.

```python
my_secong_gen = (x*2 for x in my_list)
```
##  Sets
**Un pequeño resumen**:

Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

-   Los sets son  **inmutables**
    
-   Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento
    
-   los sets guardan los elementos en desorden
    

Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}

```python
# set de enteros
my_set = {1, 3, 5}
print(my_set)

# set de diferentes tipos de datos
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set)

```

Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:

-   **add():**  nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
-   **update():**  nos permite agregar múltiples elementos al set
-   **remove():**  permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
-   **discard():**  permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
-   **pop():**  permite eliminar un elemento del set, pero lo hará de forma aleatoria.
-   **clear():**  Limpia completamente el set, dejándolo vació.

```python
#ejemplo de operaciones sobre sets 
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 

#añadiendo un elemento al set 
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set 
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 

```

Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método  **set**:

```python
#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple: ('hola', 'hola', 1, 2)
my_set2: set(my_tuple)
print(my_set2) #Output {'hola', 1}
```



