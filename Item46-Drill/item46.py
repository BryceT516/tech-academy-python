#1. Using the range function to produce the numbers 0 to 3 on separate lines
print ("1. using range(4) to get the numbers")
for x in range(4):
    print(x)
    
#2. Using the range function to produce a count down of numbers on the same line
print ("\n2. using range(3, -1, -1) to get the numbers")
for x in range(3, -1, -1):
    print(x, end=" ")
else:
    print("")

#3. Using the range function to get the numbers 8 to 2 counting down by 2s on the same line
print ("\n3. using range(8, 0, -2) to get the numbers")
for x in range(8, 0, -2):
    print(x, end=" ")
else:
    print("")
    
