from Database_Email import delete_email_data
import sqlite3
import Speak as s

conn=sqlite3.connect('classes.db')
c=conn.cursor()

def database_class():
    class_data=[('Monday',9),('Monday',1),('Monday',4),('Monday',5),
                ('Tuesday',9),('Tuesday',1),('Tuesday',4),
                ('Wednesday',1),('Wednesday',2),('Wednesday',3),
                ('Thursday',11),('Thursday',3)]

    c.execute("""
    CREATE TABLE  IF NOT EXISTS class_timings (
    Days varchar(10) not null ,
    At_time int not null
    )""")


    c.executemany('INSERT INTO class_timings Values(?,?)',class_data)
    conn.commit()



def insert_class_timings():
    flag=True
    while flag:
        s.speak("to insert data into class database")
        s.speak("Enter the class Day")
        day=input()
        s.speak("Enter timings of class")
        timing=input()
        data=[day,timing]
        c.execute('INSERT INTO class_timings Values(?,?)',data)
        conn.commit()
        s.speak("want to add another class")
        commond=s.getmy_audio()
        if 'no' in commond:
            flag=False




def display_class_database():
    for row in c.execute(' SELECT * FROM class_timings'):
        print(row)


def delete_all_class_data():
    s.speak("Are you sure want to delete all the database")
    command=s.getmy_audio()
    if 'yes' in command:
        c.execute('drop table class_timings')  #for deleting entire table data
        conn.commit()



def delete_class_data():
    s.speak("to delete the record of data in class database")
    s.speak("Enter day")
    day=input()
    s.speak("timings of class")
    timing=int(input())
    c.execute("DELETE FROM class_timings  WHERE Days='%s' AND At_time='%i' "%(day,timing))
    conn.commit()



conn.close()