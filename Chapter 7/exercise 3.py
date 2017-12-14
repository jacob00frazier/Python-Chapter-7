# Jacob Frazier CH 7 EX 3

'''
Exercise 3: Sometimes when programmers get bored or want
to have a bit of fun, they add a harmless Easter Egg to their
program Modify the program that prompts the user for the file 
name so that it prints a funny message when the user types in 
the exact file name "na na boo boo". The program should behave 
normally for all other files which exist and don't exist. Here 
is a sample execution of the program:
'''
name = input("what is the file name: ")
if name == "na na boo boo":
	print("NA NA BOO BOO TO YOU - You have been punk'd!")
	
else:
        file = open(name)
	total = 0
	line_count = 0

	for line in file:
		line = line.rstrip()
		# Skip 'uninteresting lines'
		if not line.startswith("X-DSPAM-Confidence:"):
			continue
		# Process our 'interesting' line
		colon = line.find(":")
		new_string = str(line[colon+1:])
		final_string = float(new_string)
		total += float(new_string)
		line_count += 1

	avg = total/line_count
	print(avg)
        
