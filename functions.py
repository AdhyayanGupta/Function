def countWordsFromFile():
    name = input("Input the file name")
    numberOfWords = 0

    file = open(name,'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words: ")
    print(numberOfWords)

countWordsFromFile()


    