# PIP
PIP (Package Installer for Python) es un módulo que nos permitirá instalar módulos que no vienen incluidos con Python.

Para instalar pip, hacemos
_sudo apt install python3-pip_

Para ver los paquetes que tenemos instalados, hacemos
_pip freeze_

Para instalar un módulo, basta con
_pip install <modulo>_

Ahora, para compartir nuestro proyecto con otro desarrolladora/or (porque esa persona necesita nuestros mismos módulos con las mismas versiones) se hace
_pip freeze > requirements.txt_
Lo que se logra con esto es guardar en un txt todos los módulos y las versiones de nuestro proyecto.

Para que la persona que va a trabajar con nuestro proyecto se baje todos los requerimientos, debe hacer
_pip install -r requirements.txt_
Con esto, se le instalará todo en nuestro entorno.