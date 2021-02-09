# Given an array, 
#find the average of all contiguous subarrays of size ‘K’ in it.

def find_contiguous_subarraysK(K,arr):
	result = []
	for i in range(len(arr)-K+1):
			#find the sum of the next K elements
			_sum = 0.0
			for j in range(i, i+K):
				_sum+=arr[j]
			result.append(_sum/K)

	return result

results = find_contiguous_subarraysK(5, [1,3,2,6,-1,4,1,8,2])
print("Averages of all contiguous subarrays of size K: ", results)