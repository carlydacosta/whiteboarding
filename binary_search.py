def binarySearch(alist, num):
	first = 0				# a pointer, first, at index at begining of list
	last = len(alist)-1		# a pointer, last, at index at end of list
	found = False

	while first <= last and not found:	# look for num until my first pointer moves beyond my last pointer, or vice versa, or the num is found
		mid = (first + last) // 2		# find the midpoint index
		if alist[mid] == num:			# if the number at the midpoint index is the num I'm looking for, then found = true.
			found = True

		else:							# otherwise I did not find the number
			if alist[mid] > num:		# check if the midpoint is greater than the num I'm looking for
				last = mid - 1			# if it is, then I can move the pointer at last to the left where my midpoint was, -1 since I already checked midpoint itself
			else:
				first = mid + 1			# otherwise I know my midpoint is less than the num I'm looking for, so I can move the pointer to the right +1.
	return found
