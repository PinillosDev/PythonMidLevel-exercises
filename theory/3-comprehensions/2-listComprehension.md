# List comprehension
Cuando queremos crear una lista, podemos hacerlo de varias formas. Hoy aprenderemos a hacerlo de una manera rápida y sencilla.
List comprehension o comprensión de listas es crear una lista con x valores e incluso con condiciones en una única línea.

Sigue la siguiente estructura.


_odd = [element for element in range(1, 11)]_
  |        |                |
lista      |                |
           |                |
    Elemento con que        |
    se llenará la lista     |
                            |

                for element in range(1, 11)
        Aquí se indica que por cada valor de element
        (1 en la primera iteración, 2 en la segunda, etc)
        se agregará ese valor a la lista


Ahora, si se quiere agregar una condición, por ejemplo que solo se agregue el elemento si es par, se hace
_odd = [element for element in range(1, 11) if element%2 == 0]_