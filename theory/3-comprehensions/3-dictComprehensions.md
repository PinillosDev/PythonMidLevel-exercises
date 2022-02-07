# Dictionary comprehension
Lo mismo que una list comprehension pero con diccionarios jsjs
Sigue la siguiente estructura:

_{key:value for value in iterable if condition}_
Cabe aclarar que el iterable puede ser desde un range hasta una lista o un diccionario.

def main():
    myDict = {i:i**3 for i in range(1, 101) if i%3 != 0}
    return print(myDict)

if __name__ == "__main__":
    main()