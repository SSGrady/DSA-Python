 # two pointer method
 ## one slow that changes by dupe
 ### one fast that iterates
def removeDuplicates(nums):
	if len(nums) == 0: return 0
	if len(nums) == 1: return 1

	j = 1 # slow index
	for i in range(1, len(nums)):
		if nums[i] != nums[i-1]:
			nums[j] = nums[i]
			j+=1

	for  delete_num in range(i, j-1, -1):
		del(nums[delete_num])

	return j

def main():
	return

if __name__ == '__main__':
	main()
	nums = [1,1,2,4,4]

	print(removeDuplicates(nums), " & array:", nums)
