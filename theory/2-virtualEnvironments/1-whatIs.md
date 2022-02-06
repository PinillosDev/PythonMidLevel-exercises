Antes, mejor recordar el concepto de módulos:
Un módulo es código escrito por otra persona que nos sirve. Es para no re-inventar la rueda.
Ese módulo lo podemos 'importar' en nuestro programa y usarlo.

# ¿Qué es un entorno virtual?
Es como una caja, donde tienes diferentes versiones de Python y donde puedes instalar diferentes módulos para tener royectos aislados y trabajar sin errores.
Los entornos se crearon porque a menudo al trabajar sobre varios proyectos significa enfrentarse a problemas de compatibilidad.
Es por esto que lo mejor es tener una caja donde tenemos una versión de Python y allí instalar paquetes que requieren esa versión
específica de Python.

# Instalación UBUNTU 20.04:
Para crear un entorno virtual, primero se debe habilitar *ensurepip*
_sudo apt install python3.8-venv_


Para crear un entorno virtual, se hace
_python3 -m venv venv_

-m -> llamar un módulo
venv -> virtual enviorment, este es el módulo que se llamará
venv -> el nombre que le vamos a poner, por convención es el mismo (venv)

Para activar el entorno virtual se hace
_source venv/bin/activate_
Para desactivar se hace _deactivate_

Sin embargo, podemos crear un alias, para no tener que poner toda la ruta:
_alias avenv="source venv/bin/activate"_
avenv porque *activate venv*