def sing_song():
	for i in range(99, 0, -1):
		print_part(i)
	print_ending()
			
def print_part(amount):
	single = "bottle of beer"
	many = "bottles of beer"
	left_form = many
	form = many
	left = amount-1
	
	if amount == 2:
		left_form = single
	elif amount == 1:
		form = single
		left = "no more"	
		
	print(amount, form, "on the wall,", amount, form, end="")
	print(".")
	print("Take one down and pass it around,", left, left_form, "on the wall.")
	print()
		
def print_ending():
	print("No more bottles of beer on the wall, no more bottles of beer.")
	print("Go to the store and buy some more, 99 bottles of beer on the wall.")
		
sing_song()