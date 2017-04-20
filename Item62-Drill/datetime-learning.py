from datetime import datetime, timedelta, tzinfo, time
import re

time_pattern = re.compile('^[0-1]?[0-9]:[0-5]?[0-9] ?[aApP][mM]?')


class GMT0(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=0) + self.dst(dt)
    
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
        return "GMT"

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

class GMT_8(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-8) + self.dst(dt)
    
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
        return "GMT -8"


def parse_input(inputTime):
    if(time_pattern.match(inputTime)):
        #Get the hours, minutes, and am/pm from the input
        split1 = re.split(':', inputTime)
        #print (split1)
        split2 = re.split('[aApP][mM]?', split1[1])
        #print split2
        split3 = re.split('[0-9]?[0-9]', split1[1])

        hours = split1[0]
        minutes = split2[0]
        am_pm = split3[1]

        #print (hours + ' hours, ' + minutes + ' minutes, ' + am_pm)
        return [hours, minutes, am_pm]
        
    else:
        #Not a valid time input
        return False





def start():
    gmt_0 = GMT0()
    gmt_5 = GMT_5()
    gmt_8 = GMT_8()

    current_day = datetime.now(gmt_8)
    ldn_current_day = datetime.now(gmt_0)

    pdx_open = datetime.combine(current_day,time(9, 0, tzinfo=gmt_8))
    pdx_close = datetime.combine(current_day, time(21, 0, tzinfo=gmt_8))
    ny_open = datetime.combine(current_day,time(9, 0, tzinfo=gmt_5))
    ny_close = datetime.combine(current_day, time(21, 0, tzinfo=gmt_5))
    ldn_open = datetime.combine(ldn_current_day,time(9, 0, tzinfo=gmt_0))
    ldn_close = datetime.combine(ldn_current_day, time(21, 0, tzinfo=gmt_0))
    
    continue_loop = True

    while(continue_loop):
        #Get the time from the user
        inputTime = raw_input("Enter a Portland, OR time (h:mm am/pm): ")


        time_data = parse_input(inputTime)
        if(not time_data):
            print("Enter a valid time...")
            continue
        
        if (int(time_data[0]) == 12):
            if(time_data[2] == 'am'):
                time_data[0] = str(0)
            
        elif (time_data[2] == 'pm'):
            time_data[0] = str(int(time_data[0])+12)
            

        
        time_value = time(int(time_data[0]), int(time_data[1]), tzinfo=gmt_8)
        dt1 = datetime.combine(current_day, time_value)
        #dt1 = datetime.now(gmt_8)
        
        
        #print "Portland: {}".format(dt1.time())
        print "Portland: {}".format(dt1.strftime("%I:%M%p"))

        if (dt1 >= pdx_open and dt1 < pdx_close):
            print ("Open")
        else:
            print ("Closed")


        dt2 = dt1.astimezone(GMT_5())
        
        #print (dt2.time())
        print "New York: {}".format(dt2.strftime("%I:%M%p"))

        if (dt2 >= ny_open and dt2 < ny_close):
            print ("Open")
        else:
            print ("Closed")
        
        
        dt3 = dt1.astimezone(GMT0())
        #print (dt3)
        print "London: {}".format(dt3.strftime("%I:%M%p"))

        if (dt3.time() >= ldn_open.time() and dt3.time() < ldn_close.time()):
            print ("Open")
        else:
            print ("Closed")


        response = raw_input("\nCheck another time? y/n: ")
        if (response == 'y'):
            continue_loop = True
        else:
            continue_loop = False





            

if __name__ == "__main__":
    start()
    
