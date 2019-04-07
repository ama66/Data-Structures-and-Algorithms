###Product of Array Except Self (Leetcode #238)
def ProductExceptNum(L):
	## build up prefixes for products of numbers before and including a given index
	prefix_prod=[]
	for num in L: 
		if prefix_prod: 
			prefix_prod.append(prefix_prod[-1]*num)
		else:
			prefix_prod.append(num) # Edge Case for first index where prefix_prod list is empty



	suffix_prod=[]
	for num in reversed(L):
		if suffix_prod:
			suffix_prod.append(suffix_prod[-1]*num)
		else:
			suffix_prod.append(num)

#	suffix_prod = [i for i in  reversed(suffix_prod)]
	suffix_prod = list(reversed(suffix_prod))

	Result=[]
	for i in range(len(L)):
		# Edge Cases
		if i==0:
			Result.append(suffix_prod[1])
		elif i==len(L)-1:
			Result.append(prefix_prod[-2])
		else:
			Result.append(prefix_prod[i-1]*suffix_prod[i+1])

	return Result

 
L=[3,4,5,6]

print("List is:", L)

print("Product except self is " , ProductExceptNum(L))
