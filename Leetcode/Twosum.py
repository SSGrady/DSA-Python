def twoSum(nums, target):
	prevMap = {}
	for i, n in enumerate(nums):
		if target-n in prevMap:
			return [prevMap[target-n], i] #returns index of difference, index current
		prevMap[n] = i
	return ## O(N)

def twoSumII(numbers, target):
	prevHash = {}
	for i,n in enumerate(numbers):
		if target-n in prevHash:
			return [prevHash[target-n],i+1]
		prevHash[n] = i+1
	return


def twoSums(nums, target):
	for i in range(len(nums)-1):
		for x in range(len(nums)):
			if x!=i and nums[x] + nums[i] == target:
				return [i,x]
				## O(N^2)
def main():
	return

if __name__ == '__main__':
	main()
	nums = [2,7,11,15,20,4,8]
	nums1 = [6,10,9,3,2,1,5]
	nums2 = [4,5,8,13,12,11]
	target = 19
	print(twoSumII(nums,target))
	print(twoSumII(nums1,target))
	print(twoSumII(nums2,target))
	## enumerate returns (index, value)
	