#!/Users/user/.pyenv/shims/python

l1 = [0,1,2,3,4,5]

pt = prt = len(l1) - 2
print(l1)
while (pt >= 0):
	# if any elements to the right of index are greater than element at index
	if any(x > l1[pt] for x in l1[pt + 1:]):
		#sort the elements to the right of index
		rhsorted = sorted(l1[pt + 1:])
		l1 = l1[0:pt+1] + rhsorted

		#take lowest greater than the index value and swap with index
		first_grt = next((n for n in rhsorted if n > l1[pt]), None)
		rloc = rhsorted.index(first_grt)
		tmp = l1[pt]
		l1[pt] = l1[pt + rloc + 1]
		l1[pt + rloc + 1] = tmp

		# then print
		print(l1)

		#then reset the pointer to the far right and start over
		pt = prt
	else:
		#shift index left by one and start over unless we are already at far left and are done.
		pt -= 1
