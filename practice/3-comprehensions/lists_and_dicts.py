def main():
    myList = [1, 'Hello', True, 4.5]
    myDict =  {
        "firstName": "Juan",
        "lastName": "Pinillos"
    }

    superList = [
        {"firstName": "Juan",
        "lastName": "Pinillos"},
        {"firstName": "María",
        "lastName": "Tobar"},
    ]

    superDict = {
        "numbers": [1, 2, 3, 4, 5],
        "bool": [True, False]
    }

    for key, value in superDict.items():
        print(f"{key} -> {value}")

if __name__=='__main__':
    main()