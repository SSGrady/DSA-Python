def threeSum(nums):
	prevHash, solutionHash = {}
	for i,n in range(len(nums)):
		difference = nums[i+1] - nums[i]
		if difference in prevHash:
			solutionHash.append(prevHash[i], nums[i+1], nums[i])
	return [solutionHash]

def main():
	return

if __name__ == '__main__':
	main()
	nums = [-1,0,1,2,-1,4]
	print(threeSum(nums))