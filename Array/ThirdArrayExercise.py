"""Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function"""

def main():
	max = int(input("What is max?"))

	"""all_odds = list(range(1,max))
	for i in range(len(all_odds)-1):
		if all_odds[i] % 2 == 0:
			all_odds.remove(all_odds[i])
		if i == len(all_odds)-1:
			break

	print(all_odds)"""                #  this is correct but innefficient
									 # now then..
	odd_numbers = []
	for i in range(max):
		if i%2 !=0:
			odd_numbers.append(i)
		
	print("Odd numbers", odd_numbers)


if __name__ == '__main__':
	main()