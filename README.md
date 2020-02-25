# Libreria de vectores y matrices de complejos
Proyecto de CNYT Ciencias naturales y tecnologia. Repositorio con el objetivo de solucionar los problemas principales sobre las operaciones de complejos
# Descripción de contenido
En el proyecto se hacen diferentes casos de operaciones sobre los complejos incluyendo entre vectores y matrices. Se utilizara al estilo de calculadora de complejos.
```
import LibCom
LibCom.suma(complejo 1, complejo 2)
```
Tener claro que los complejos seran escritos en forma de tuplas. Ejemplo:
```
2 + i = (2,1)
```
# Requisitos 
Los requisitos son solamente contar con el lenguaje de programación Python(IDLE) para poder ejecutar la libreria y utilizarla.
# Instalacion 
Para la instalación es necesario descargar el codigo LibCom y TestLibCom luego si desea en un nuevo proyecto de python con solo importar la libreria de esta forma:
```
import Libcom
```
Lograra acceder a la calculadora de numeros complejos y desarrollo de los mismos con solo poner la función que desea realizar. Ejemplo:
```
LibCom.suma((1,2),(2,4))
```
Ejecutando el programa le aparece el resultado y así mismo con resta multiplicacion, producto como se encuente la función descrita.
# Pruebas
Las pruebas en el archivo de TestLibCom puede reemplazar en los vectores 'u' y 'v' (o matrices) y a continuación ejecutando el programa se le mostrara el resultado final de la operación en cuya funcion halla reemplazado los vcetores. Las funciones vendran de este modo. 
```
def test_suma(self):
        u = (3, 5)
        v = (5, 6)
        self.assertEqual(LibCom.suma(u, v), (8, 11))
```
En este caso se realiza la suma de dos numeros complejos.
en las ultimas casillas del ejemplo anterior donde en este caso esta '(8, 11)' se refiere al resultado esperado, este tendra que ser modifciado dependiendo de los complejos asignados por el usuario, prueban si la respuesta esta correcta o incorrecta. En el caso de estar incorrecta se le mostrara el resultado verdadero.
# Construido con:
Este proyecto fue hecho con el lenguajede  de programacion python y con informacion de internet sobre numeros complejos.
# Autores
Juan Pablo Sánchez Suárez
Estudiante de la Escuela Colombiana de Ingenieria Julio Garavito
Materia : Ciencias Naturales y Tecnologia (CNYT)


