from datetime import timedelta, datetime, tzinfo
import re

time_pattern = re.compile('^[0-1]?[0-9]:[0-5]?[0-9] ?[aApP][mM]?')

class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)
    
    def dst(self, dt):
        #DST starts Last Sunday in March
        d = datetime(dt.year, 4, 1) # ends Last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return "GMT +1"

class GMT_5(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-5) + self.dst(dt)
    
    def dst(self, dt):
        #DST starts Last Sunday in March
        d = datetime(dt.year, 4, 1) # ends Last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return "GMT -5"



def parse_input(inputTime):
    if(time_pattern.match(inputTime)):
        #Get the hours, minutes, and am/pm from the input
        split1 = re.split(':', inputTime)
        print (split1)
        split2 = re.split('[aApP][mM]', split1[1])
        print split2
        split3 = re.split('[0-9]?[0-9]', split1[1])

        hours = split1[0]
        minutes = split2[0]
        am_pm = split3[1]

        print (hours + ' hours, ' + minutes + ' minutes, ' + am_pm)
        return [hours, minutes, am_pm]
        
    else:
        #Not a valid time input
        return False


def london_time(pdx_time):
    # London time is +8 hours from Portland
    new_hours = pdx_time[0] + 8
    if (new_hours > 24):
        new_hours = new_hours - 24
        if (new_hours < 12):
            new_am_pm = 'am'
        else:
            new_am_pm = 'pm'

    return[new_hours, pdx_time[1], new_am_pm]




def start():
    continue_loop = True

    while(continue_loop):
        print ()
        #Prompt the user for a time:
        inputTime = raw_input("Enter a Portland, OR time (h:mm pm): ")

        #parse the input to get the entered time.
        time_data = parse_input(inputTime)
        if (time_data == False):
            print ("Please enter a valid time")

        else:
            #Create a time value using the parsed info
            if(time_data[2] == 'pm'):
                new_hours = str(int(time_data[0]) + 12)
                time_data[0] = new_hours
                
            pdx_time = time(int(time_data[0]), int(time_data[1]), tzinfo=gmt8)
            print ('pdx time:')
            print (pdx_time)
            
            #Use the datetime module functions to get the corresponding
            # times in New York and London

            #Print each city and the time in that location and either
            # Open or Closed depending on if the time is during open hours.


        continue_response = raw_input("\nCheck another time? y/n: ")
        if (continue_response == 'n'):
            continue_loop = False
        else:
            continue_loop = True











if __name__ == "__main__":
    start()
