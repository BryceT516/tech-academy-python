epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds' : 'lt@gmail.com',}

# Adds a different email address
epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'

print 'New email for Tim: ' + epic_programmer_dict['Tim Berners-Lee']

# Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'

# Add Sergey Brin and myself to the dictionary
epic_programmer_dict['Sergey Brin'] = 'sb@gmail.com'
epic_programmer_dict['Bryce Tucker'] = 'bt@gmail.com'

print "Before delete: "
print epic_programmer_dict

# Delete Sergey Brin and another from the dictionary
del epic_programmer_dict['Sergey Brin']
del epic_programmer_dict['Guido van Rossum']


print "After delete: "
print epic_programmer_dict

