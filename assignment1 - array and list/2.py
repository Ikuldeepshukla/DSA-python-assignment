# Given a list of hetrogeneous elements. Write a python script to remove all non int values from the list.

def removeNonInt(inputList):
    n = len(inputList)
    for index in range(n-1, -1, -1):
        if not isinstance(inputList[index], int):
            inputList.remove(inputList[index])

    return inputList

dummyInput = [1,2,4,"we", 2, "r", 6, "w"]

print(removeNonInt(dummyInput))
