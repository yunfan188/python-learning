from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease input your first name: ")
	if first == 'q':
		break
	last = input("Please input your last name: ")
	if last == 'q':
		break
	
	formatted_name = get_formatted_name(first, last)
	print("\tNeatle formatted name: "+ formatted_name+ ".")
