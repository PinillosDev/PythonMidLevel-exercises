def main():
    myDict = {i:i**3 for i in range(1, 101) if 1%3 != 0}
    return print(myDict)

if __name__ == "__main__":
    main()