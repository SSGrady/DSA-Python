""" 1. Let us say your expense for every month are listed below,
		January - 2200
		February - 2350
		March - 2600
		April - 2130
		May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""
def main():
	exp = [2200,2350,2600,2130]
	# Problem 1
	print("In Feb, I spent ",(exp[1]-exp[0]), " dollars") #150
	# Problem 2
	print("This first quarter my total expenses came out as ", (exp[0]+exp[1]+exp[2])) #7150
	# Problem 3
	print("Did I spend $2000 in any given month? --> ", 2000 in exp) # False
																	## remember "in" operator checks
																	### to see if a value exists in a sequence
	# Problem 4
	exp.append(1980)
	print("Expenses at the end of June", exp) #[2200, 2350, 2600, 2130, 1980]
	# Problem 5
	exp[3]-= 200
	print("Expenses after a $200 refund in April", exp) # [2200, 2350, 2600, 1930, 1980]

	################################################################# 
	

if __name__ == '__main__':
	main()
