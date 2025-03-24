def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Left half of the array
        right_half = arr[mid:]  # Right half of the array

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merging two sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):  # Compare elements and merge
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):  # Copy any remaining elements from left_half
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):  # Copy any remaining elements from right_half
            arr[k] = right_half[j]
            j += 1
            k += 1

    #print(arr)

list1 = [9,5,1,3,7,8,4,6]
merge_sort(list1)
print(list1)