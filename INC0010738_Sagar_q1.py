def arrayMaxConsecutiveSum(array,num):

	first = sum(array[0:num])
	highest = first
	for i in range(num,len(array)):
		first = first - array[i-num] + array[i]
		if first > highest:
			highest = first
	return highest
    
print (arrayMaxConsecutiveSum([2,1,4,6,8,5,7,9,3,11],3))
