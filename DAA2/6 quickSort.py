def partition(array, low, high):
  pivot = array[high]
  
  pivotIndex = low 
  for i in range(low, high):
    if array[i] < pivot:
                 # arr[i]               #pIndex
      # (smaller than pivot) swap (greater than pivot) 
      (array[pivotIndex], array[i]) = (array[i], array[pivotIndex])
      pivotIndex = pivotIndex + 1

  # swap pIndex and pivot
  (array[pivotIndex], array[high]) = (array[high], array[pivotIndex])

  return pivotIndex

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array:")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)