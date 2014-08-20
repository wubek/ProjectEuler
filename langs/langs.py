import re

write_file = open("output.txt", "w")
counter = 0

with open("bhaarat.txt", "r") as read_file:
	for line in read_file:
		word = line.split(".")
		if re.search(' [H,S].*$', word[1]):
			counter += 1
			write_file.write(str(counter) + "." + word[1])

with open("bhaarat.txt", "a") as file:
	file.write("\n" + str(int(word[0])+1) + ". English")
			
write_file.close()