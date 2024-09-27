import sqlite3
import Speak as s
import smtplib


conn=sqlite3.connect('classes.db')
c=conn.cursor()


def email_gui():
    reciever=input("enter email-id: ")
    reciever=input()
    sent_mail(reciever)

def check_database(reciever):
    s.speak("checking in your data base")
    for row in c.execute('SELECT * FROM emails'):
        if(row[0]==reciever):
            s.speak("hey i got it mail id")
            sent_mail(row[1])
            return 0
    return 1


def mail_validation(reciever):
    flag=True
    count=0
    reciever=reciever.lower()
    if(check_database(reciever)):
        s.speak("I think message need to send others")
        flag=True
        count=0                                                                                                                                     
        while flag:
            s.speak("removing spaces in sender mail")
            reciever=reciever.replace(" ","")
            s.speak("Checking validation of mail")
            if(len(reciever)>=11):
                s.speak("Length is valid")
                if '@' in reciever:
                    reciever=reciever.split('@')
                    reciever.pop(1)
                    reciever=reciever[0]
                    s.speak("I am checking @ split")
                elif 'attherateof' in reciever:
                    change='attherateof'
                    reciever=reciever.replace(change,'@')
                    reciever=reciever.split('@')
                    reciever.pop(1)
                    reciever=reciever[0]
                    s.speak("Removing at the rate of word")
                else:
                    s.speak("Everything is fine")
                        
            if(reciever[:-10]!="@gmail.com"):
                reciever+="@gamil.com"
                s.speak("domain has been addded")
            reciever=reciever.lower()        
            s.speak(reciever)
            s.speak("Does the reciever name is correct?")
            check=s.getmy_audio()

            if 'yes' in check:
                sent_mail(reciever)
                flag=False
            else:
                if(count==1):
                    s.speak("Sorry i am unable to understand")
                    s.speak("Enter in my terminal i will take care rest")
                    email_gui()
                    flag=False
                else:
                    s.speak("Tell me again reciever mail")
                    reciever=s.getmy_audio()
                    count+=1
                      

def sent_mail(reciever):
    try:
        s.speak('What should I say? ')
        content = s.getmy_audio()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        sender='ravitejanandam1999@gmail.com'
        password='raviap07bt5697'
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender,reciever, content)
        server.close()
        s.speak('Email sent!')
    except Exception as e:
        s.speak('Sorry Sir! I am unable to send your message at this moment!')
        print(e)
                

