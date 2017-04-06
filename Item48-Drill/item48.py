# Creating a function that will accept a list and return a sorted version of the list.
# The list will be of numbers.
# The resulting sorted list will be in ascending order.


testList1 = [67, 45, 2, 13, 1, 998]
testList2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]


def mySort(inputList):
    outputList = []
    for x in inputList:
        if not outputList:
            #ouputList is empty, so just add the given value
            outputList.append(x)
        else:
            #The outputList is not empty, so figure out where this new number goes
            for i, y in enumerate(outputList):
                if x < y:
                    #The new number is less than this number, so place it before.
                    outputList.insert(i, x)
                    break
            else:
                #If the for loop terminates without having a break event, then the new number is larger
                # than all the numbers in the outputList, so add it at the end
                outputList.append(x)


    return outputList
# -- End of mySort()



print (mySort(testList1))
print (mySort(testList2))
