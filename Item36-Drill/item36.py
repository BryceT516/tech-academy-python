#1. Assign an integer to a variable
print "\n1. Assigning an integer to a variable..."
intVar = 42

#2. Assign a string to a variable
print "\n2. Assigning a string to a variable..."
strVar = "A string variable"

#3. Assign a float to a variable
print "\n3. Assigning a float to a variable..."
fltVar = 3.14

#4. Use the print function and .format() notation to
#    print out the variable you assigned
print "\n4. Printing out the values of the variables..."
print ("Integer variable 'intVar' has the value {},\n"
       "String variable 'strVar' has the value: {},\n"
       "Float variable 'fltVar' has the value: {}.".format(intVar, strVar, fltVar))

#5. Use each of these operators: +, -, *, /, +=, =, %
print "\n5. Using each of these operators: +, -, *, /, +=, =, %"
print ("Using '+': 5 + 8 = {}".format(5+8))
print ("Using '-': 5 - 8 = {}".format(5-8))
print ("Using '*': 5 * 8 = {}".format(5*8))
print ("Using '/': 15 / 8 = {}".format(15/8))
intVar = 8
print ("Using '=': intVar = 8, makes intVar equal {}".format(intVar))
intVar += 8
print ("Using '+=': intVar += 8, makes intVar equal {}".format(intVar))
print ("Using '%': 15 % 8 = {}".format(15%8))

#6. Use each of these logical operators: and, or, not
print "\n6. Using and, or, and not..."
print "True and True is {}".format(True and True)
print "False and True is {}".format(False and True)
print "True and False is {}".format(True and False)
print "False and False is {}".format(False and False)
print "True or True is {}".format(True or True)
print "False or True is {}".format(False or True)
print "True or False is {}".format(True or False)
print "False or False is {}".format(False or False)
print "not True is {}".format(not True)
print "not False is {}".format(not False)

#7. Use each of these conditional statements: if, elif, else
print "\n7. Using if, elif, and else..."
counter = 0;
stopLoop = False
while not stopLoop:
    if counter < 3:
        print ("counter is less than 3: counter = {}".format(counter))
        counter += 1
    elif counter >=3 and counter < 6:
        print ("counter is over 3 and less than 6: counter = {}".format(counter))
        counter += 1
    else:
        print ("counter is over 6, so stop counting: counter = {}".format(counter))
        counter += 1
        stopLoop = True

        
#8. Use a while loop
print "\n8. Using a while loop..."
stopLoop = False
counter = 0
while not stopLoop:
    if counter < 10:
        print ("Looping in a while loop. Counting as we go: counter = {}".format(counter))
        counter += 1
    else:
        stopLoop = True
        print ("Looped 10 times, stopping now. Setting stopLoop to True.")



#9. Use a for loop
print "\n9. Using a for loop..."
print "A for loop that counts from 0 to 100 by 10s:"
for x in range(0, 100, 10):
    print x

#10. Create a list and iterate through that list using a for loop to
#     print each item out on a new line
print "\n10. Creating a list... Displaying it using a for loop:"
list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for x in list_a:
    print x

#11. Create a tuple and iterate through it using a for loop to
#     print each item out on a new line
print "\n11. Creating a tuple... displaying each item using a for loop:"
tupleOne = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for x in tupleOne:
    print x

#12. Define a function that returns a string variable
print "\n12. Defining the function getString()"
def getString():
    return "This is a string from getString()!"

#13. Call the function you defined above and print the result to the shell
print "\n13. Calling the getString function:"
print getString()

