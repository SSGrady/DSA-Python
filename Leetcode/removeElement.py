def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[count] = nums[i]
            count+=1
    return count

def main():
    return

if __name__ == '__main__':
    main()
    nums = [3,2,2,3]
    val = 3
    print(removeElement(nums,val))