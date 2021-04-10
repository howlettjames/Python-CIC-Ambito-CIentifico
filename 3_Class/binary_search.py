def binarySearch(array, value, inferior = 0, superior = None):
    if superior == None:
        superior = len(array) - 1

    if superior >= inferior:
        middle = (inferior + superior) // 2
        if array[middle] == value:
            return middle
        elif value < array[middle]:
            return binarySearch(array, value, inferior, middle - 1)
        else:
            return binarySearch(array, value, middle + 1, superior)
    else:
        return None

lista = [3, 5, 7, 8, 23, 25, 28, 30, 45, 1500]
print(lista)
print(binarySearch(lista, 30))