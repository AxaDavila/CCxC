# CCxC
Test in enviroment qa


En dado caso es necesario que antes de correr el test,  en la terminal envie los siguientes comandos:

pip install webdriver-auto-update
Para Python
pip install python 
python.exe -m pip install --upgrade pip
o puede guiarse por el siguiente artitulo: https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html

El archivo CCxC realizará la sieguiente prueba:

Crear un nuevo User:

Precondiciones:
- User con permisos de Admin.

Criterios de Aceptación:
- Solo debe habilitarse la pestaña de creación a un usuario Admin
- los usuarios creados deben tener la opción de habilitado/deshabilitado
- el password debe contener caracteres en mayúscula, minúscula simbolos y numeros

El usuario ingresa al sub menu Admin
El usuario elije la opción del tab User Managment /Users
El usuario ingresa los siguientes datos para crear un nuevo usuario
*(title) System Users
- opción: ADD User
Username: Prueba
User Role: (null)
Employee Name: Arnulfo pruebas
Status: Enabled
Password:12345Admin*
Confirm Password:12345Admin*
El resultado será (Invalido), debe notificar al actor los valores requeridos.

El archivo test realizará la siguiente prueba:

Validar campos obligatorios en Corporate Branding.
Precondiciones:
User con permisos de Admin.

Criterios de aceptación:
Los cambios deben producirse inmediatamente
debe completarse los campos obligatorios y habilitarse el boton "publish".

el usuario debe seleccionar submenu Admin, y luego tab "Corporate Branding"
el usuario selecciona los campos obligatoriios que tienen un asterisco (*), en su título:
el usuario oprime input "Primary Color*", y selecciona el color de la paleta de colores.
el usuario oprime input "Secondary Color*", y selecciona el color de la paleta de colores.
el usuario oprime input "Primary Font Color*", y selecciona el color de la paleta de colores.
el usuario oprime input "Secondary Font Color*", y selecciona el color de la paleta de colores.
el usuario oprime input "Primary Gradient Color 1*", y selecciona el color de la paleta de colores.
el usuario oprime input "Primary Gradient Color 2*", y selecciona el color de la paleta de colores.

El usuario selecciona la opción de "publish" para guardar y mostrar cambios.
(el resultado será exitoso)

