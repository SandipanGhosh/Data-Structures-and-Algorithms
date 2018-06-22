"""This function selects the last element as the pivot
and places all the elements smaller than it to it's left and
all the elements greater than it to it's right."""
def partition(arr, low, high):
	i = low-1			# index of smaller element
	pivot = arr[high]	# pivot

	for j in range(low, high):

		# If current element is <= pivot then increment the lower element index
		# and swap
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	# Place pivot at the correct position
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


# Function for Quick Sort
def quick_sort(arr, low, high):
	if low < high:
		# After this step arr[pi] is at the correct position
		pi = partition(arr, low, high)

		# Recursively sort elements before and after the partition
		quick_sort(arr, low, pi-1)
		quick_sort(arr, pi+1, high)


# Test cases
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),