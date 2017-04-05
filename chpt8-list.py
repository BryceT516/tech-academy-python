'''
# Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

epic_programmer_list.append("Me")

#Print to console
for programmer in epic_programmer_list:
    print "Epic programmers: " + programmer
'''

# Create list of numbers
number_list = [1, 2, 3, 4, 5]
empty_number_list = []

# Loop to work with each number in number_list
for x in number_list:
    #Append each number to the power of 2
    # to the empty_number_list
    empty_number_list.append(x**2)
    
print empty_number_list
