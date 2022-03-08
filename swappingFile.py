def swapFileData():
    file1 = input("What is the first file name?")
    with open(file1, "r") as openFile1:
        writeFile1 = openFile1.read()
    file2 = input("What is the second file name?")
    with open(file2, "r") as openFile2:
        writeFile2 = openFile2.read()
    with open(file1, "w") as openFile1:
        openFile1.write(writeFile2)
    with open(file2, "w") as openFile2:
        openFile2.write(writeFile1)

swapFileData()

    
