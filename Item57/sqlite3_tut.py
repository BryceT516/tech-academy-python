#! Python3
# A Python tutorial by sentdex on youtube.


import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145125552, '2016-01-02', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()



def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%S')) #Converting a unix time to datestamp
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()



    
def read_from_db():
    c.execute('SELECT * FROM stuffToPlot WHERE value=3')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print (row)


def graph_data():
    c.execute("""SELECT unix, value FROM stuffToPlot""")
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '.')
    plt.show()


def update_db():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value=2')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    

def delete_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    c.execute('''DELETE FROM stuffToPlot WHERE value=99''')
    conn.commit()

    print(50 * '#')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]


#create_table()
#data_entry()

#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

read_from_db()

#graph_data()


#update_db()

#delete_from_db()

c.close()
conn.close()


















