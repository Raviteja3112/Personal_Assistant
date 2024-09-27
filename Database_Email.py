import sqlite3
import Speak as s

conn=sqlite3.connect('classes.db')
c=conn.cursor()

def database_email():
    #for inserting timing in data base .
    emails_data=[('ravi','ravitejanandam1999@gmail.com'),
    ('hari','sriharikolli98@gmail.com'),
    ('poonam','poonamrockzz30@gmail.com')]

    c.execute("""
    CREATE TABLE  IF NOT EXISTS emails (
    nick_name varchar(20) not null ,
    email_id varchar(40) not null
    )""")


    c.executemany('INSERT INTO emails Values(?,?)',emails_data)
    conn.commit()


def insert_emailid():
    conn=sqlite3.connect('classes.db')
    c=conn.cursor()
    flag=True
    while flag:
        s.speak("Enter the nick name to call")
        nick_name=input()
        s.speak("Enter mail id")
        email_id=input()
        data=[nick_name,email_id]
        c.execute('INSERT INTO emails Values(?,?)',data)
        conn.commit()
        s.speak("want to add another email")
        commond=s.getmy_audio()
        if 'no' in commond:
            flag=False
   
    



def display_email_database():
    for row in c.execute(' SELECT * FROM emails'):
        print(row)


def delete_all_email_data():
    s.speak("Are you sure want to delete all the database")
    command=s.getmy_audio()
    if 'yes' in command:
        c.execute('drop table emails')  #for deleting entire table data
        conn.commit()


def update_email_nick_name():
    s.speak("Enter nick name to update")
    name=input("Enter: ")
    s.speak("Enter new nick name to update")
    new_name=input("Enter")
    try:
        c.execute("UPDATE emails set nick_name= '%s' WHERE nick_name= '%s' " %(new_name,name))
        conn.commit()
    except Exception as e:
        s.speak(e)


def update_email_id():
    s.speak("Enter email id to update")
    name=input("Enter: ")
    s.speak("Enter new email id to update")
    new_name=input("Enter")
    try:
        c.execute("UPDATE emails set email_id= '%s' WHERE email_id= '%s' " %(new_name,name))
        conn.commit()
    except Exception as e:
        s.speak(e)


def delete_email_data():
    s.speak("Enter nick name")
    name=input()
    c.execute("DELETE FROM emails  WHERE nick_name='%s'"%(name))
    conn.commit()


conn.close()
