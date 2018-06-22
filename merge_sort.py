def merge_sort(list_to_sort):

	# list with fewer than 2 elements are already sorted
	if len(list_to_sort) < 2:
		return list_to_sort

	# divide the list in half and merge recursively
	mid_index = len(list_to_sort) // 2
	
	left = merge_sort(list_to_sort[:mid_index])
	right = merge_sort(list_to_sort[mid_index:])
	
	return merge(left,right)


def merge(left,right):
	# merge the sorted halves
	sorted_list = []
	left_indx = 0
	right_indx = 0
	
	while left_indx < len(left) and right_indx < len(right):
		if left[left_indx] < right[right_indx]:
			sorted_list.append(left[left_indx])
			left_indx += 1
		else:
			sorted_list.append(right[right_indx])
			right_indx += 1
	
	sorted_list.extend(left[left_indx:])
	sorted_list.extend(right[right_indx:])
	
	return sorted_list


# Test cases
ar_list = [8,5,2,1,6,9,3,4]
print("Unsorted list: " + str(ar_list))
print("Sorted list: " + str(merge_sort(ar_list)))
