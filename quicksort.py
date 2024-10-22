import random
import time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    startTime = time.time()
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    endTime = time.time()
    executionTime = endTime - startTime
    return array, executionTime


def randomArrays(num):
    arr = []
    
    while num != 0:
        arr.append(random.randint(0, 10000))
        num -= 1
    return arr

def bubbleSort(arr):
    startTime = time.time()
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return time.time()-startTime, arr

def getPromBubble(num):
    results = []

    for i in range(0, 10):
        x = randomArrays(num)
        timeElapsed = bubbleSort(x)
        results.append(timeElapsed[0])
    
    sum = 0
    for k in results:
        sum += results[i]

    print(sum/10)

def getPromSort(num):
    results = []

    for i in range(0, 10):
        x = randomArrays(num)
        sortedResult = quickSort(x, 0, len(x) - 1)
        results.append(sortedResult[1])
    
    sum = 0
    for k in results:
        sum += results[i]

    print(sum/10)

print("---------------------------------------------------------")
getPromBubble(1000)
getPromBubble(2000)
getPromBubble(3000)
getPromBubble(4000)
getPromBubble(5000)
print("---------------------------------------------------------")
print("---------------------------------------------------------")
getPromSort(1000)
getPromSort(2000)
getPromSort(3000)
getPromSort(4000)
getPromSort(5000)
print("---------------------------------------------------------")



