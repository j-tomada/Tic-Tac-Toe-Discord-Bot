array = []

def newList(arr):
    global array
    array = []

    for i in arr:
        array.append(i)

def nextTurn():
    returnID = array[0]
    array.pop(0)
    array.append(returnID)

def front ():
    return array[0]
