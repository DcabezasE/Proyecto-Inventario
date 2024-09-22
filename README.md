# Proyecto-inventario
## Integrantes:
-Danna Ariana Guzman Rivas
-David Alejandro Cabezas Espinosa

## Alternativa 1:
Construir una aplicación que emule una un sistema de gestión de inventario para una bodega utilizando Python.

## Definición del problema:
La gestión de inventarios en pequeños y medianos emprendimientos, como las chazas de la universidad, que una es la motivación de este proyecto, a menudo se realiza de manera manual a papel o con sistemas ineficientes, lo que puede llevar a errores en el registro de entradas y salidas de productos o desfalcos de plata, así como en el control del stock en inventario o bodega.

  ## Objetivo: 
  Desarrollar una solución automatizada que permita registrar entradas y salidas de productos de manera eficiente, actualizando el inventario en tiempo real, evitando     errores comunes en la gestión manual.

## Cómo se abordó el problema: 
Se diseñó un sistema básico de gestión de inventario en Visual Studio a base de python que permite registrar la entrada y salida de productos con opcion de interfaz grafica de usuario (GUI) y persistencia de datos. El sistema actualiza el stock en tiempo real y proporciona un informe del inventario actual. El enfoque principal fue garantizar la simplicidad y eficiencia del código para facilitar su uso en pequeños y medianos emprendimientos. La chaza de inspiración se llama Druma, ubicada en la salida de la 26, que vende accesorios, ropa, sticker, y demas cosas de diversos gustos personales, la chaza se ha visto enredada por la falta de gestion de inventario, y mal manejo a la hora de surtir, este proyecto es para ayudar a la organización, el inventariado y el registro de ventas.


## Diagrama de clases:
![Imagen de WhatsApp 2024-09-22 a las 15 56 00_1df7953a](https://github.com/user-attachments/assets/32c32b75-1672-401d-95ba-93a64c170bc9)

# Instrucciones de Instalación y Uso
Todos los comandos son en la windows powershell
-Primero, clona el repositorio desde GitHub:
```
git clone https://github.com//DcabezasE/Proyecto-Inventario.git
cd Proyecto-Inventario
```
-Crear y Activar un Entorno Virtual
Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. 
Para crearlo y activarlo, ejecuta los comandos:

```
python -m venv venv
.\venv\Scripts\activate
```

-Instalar Dependencias
Una vez que el entorno esté activado, instala las dependencias necesarias ejecutando:
```
pip install -r requirements.txt
```
Esto instalará todas las bibliotecas necesarias como openpyxl y tkinter.

-Uso del Sistema de Inventario
Para ejecutar el sistema de inventario, utiliza el siguiente comando:
```
python -m sistema_inventario
```

Esto ejecutará la interfaz gráfica del inventario y podrás interactuar con la aplicación, registrando productos y ventas, y visualizando el inventario.

-Archivo Excel:
* El inventario se guarda automáticamente en un archivo llamado inventario.xlsx en la misma carpeta del proyecto.
* Las ventas se registrarán en una hoja separada en el mismo archivo.
