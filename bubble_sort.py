def bubble_sort(ar_list):
	# Outer range will be n for first pass, (n-1) for second pass etc.
	for outer_indx in range(len(ar_list)-1, 0, -1):

		# Compare within the set range
		for inner_indx in range(outer_indx):
			if ar_list[inner_indx] > ar_list[inner_indx+1]:
				temp = ar_list[inner_indx]
				ar_list[inner_indx] = ar_list[inner_indx+1]
				ar_list[inner_indx+1] = temp
	return ar_list

# Test cases
ar_list = [8,5,2,1,6,9,3,4]
print("Unsorted list: " + str(ar_list).strip('[]'))
print("Sorted list: " + str(bubble_sort(ar_list)).strip('[]'))
