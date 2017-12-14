# Jacob Frazier CH 7 EX 2

'''
Exercise 2: Write a program to prompt for a file name,
and then read through the file and look for lines of the
form:
'''

name = input("what is the file name: ")
file = open(name)
total = 0
line_count = 0

for line in file:
    line = line.rstrip()
    
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    colon = line.find(":")
    new_string = str(line[colon+1:])
    final_string = float(new_string)
    total += float(new_string)
    line_count += 1

avg = total/line_count
print(avg)
        
