def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
    # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    
#main code
data = [2, 45, 0, 11, 9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')

for element in data:
    print(element)