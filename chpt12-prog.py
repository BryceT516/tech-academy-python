epic_programmer_dict = {'tim berners-lee' : ['tbl@gmail.com', 111],
                        'guido van rossum' : ['gvr@gmail.com', 222],
                        'linus torvalds' : ['lt@gmail.com', 333],
                        'larry page' : ['lp@gmail.com', 444],
                        'sergey brin' : ['sb@gmail.com', 555]}

print epic_programmer_dict

def searchPeople(personsName):
    #Looks up the name in the epic dictionary
    try:
        #Tries the following lines of code
        # if there are no errors then it runs

        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
        
    except:
        #If there are erros, then this code runs
        print 'No information found for that name.'
    

userWantsMore = True

while userWantsMore == True:
    #Asks user to input persons name
    personsName = raw_input('Please enter a name ').lower()

    #Run our new function searchPeople with what was
    # typed in
    searchPeople(personsName)

    #See if user wants to search again
    searchAgain = raw_input('Search again? (y/n)')
    #check what they reply with and act accordingly
    if searchAgain == 'y':
        #userWantsMore stays as true so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        #userWantsMore turns to false to stop the loop
        userWantsMore = False
    else:
        #User inputs an invalid response, so quit
        print "I don't understand what you mean, quitting"
        userWantsMore = False

