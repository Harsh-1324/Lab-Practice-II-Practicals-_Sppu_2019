3
# Greedy Algorithm - Selection Sort

def selectionSort(array):

    n = len(array)

    # Traverse through all array elements
    for step in range(n):

        min_idx = step

        # Find minimum element
        for i in range(step + 1, n):

            if array[i] < array[min_idx]:
                min_idx = i

        # Swap minimum element with current element
        array[step], array[min_idx] = array[min_idx], array[step]

        # Print each greedy step
        print(f"Step {step + 1}: {array}")


# Driver Code
data = [2, 45, 0, 11, 9]

print("Original Array:")
print(data)

print("\nGreedy Steps:")

selectionSort(data)

print("\nFinal Sorted Array:")
print(data)
---------------------------------------

Greedy choice → always picking the minimum from unsorted part
No backtracking → once swapped, never reconsidered
Time complexity → O(n²) — two nested loops
Space complexity → O(1) — in-place sorting, no extra space used
Not always globally optimal for all greedy problems — but for sorting, greedy minimum selection always gives the correct result
-------------------------------