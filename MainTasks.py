from playsound import playsound
import webbrowser
import pyautogui as p
import os
import sys
import time
import random
import wikipedia
import pyjokes
from geopy.geocoders import Nominatim
from geopy import distance
import Battery_CPU
import News 
import Speak as s
import College_Opening
from plyer import notification
import pywhatkit as kit
import Drowsiness_Detection as dd
import Gmail
import Database_Email 
import Database_Class

bot=["attend class","activate bot","mushroom","bot"]
music=['play music','i am bore','music','stop music']


def maintasks():
    while True:
        time.sleep(1)
        command=s.getmy_audio()
        command=command.lower()
        #ex:- what's the weather in phagwara
        if 'weather' in command:
            city=command.split()
            weather.weather_requests(city[-1])

        #ex:- play vibe song in youtube   
        elif 'youtube' in command:
            command=command.replace('youtube','')
            s.speak("playing video on your command")
            kit.playonyt(command)
            time.sleep(2)

        #ex:- open wordpad
        elif 'wordpad' in command:
            if 'open' in command:
                s.speak("Opening wordpad")
                os.system('start wordpad.exe')
            elif 'close' in command:
                s.speak("closing wordpad")
                os.system('TASKKILL /F /IM wordpad.exe')
                
        #ex:- open notepad.
        elif 'notepad' in command:
            if 'open' in command:
                playsound('Startup Sound.mp3')
                s.speak("Opening Notepad")
                p.press('win',interval=0.2)
                p.typewrite("Notepad",interval=0.1)
                p.press('enter',interval=0.3)
                time.sleep(2)
                s.speak('what do you want me write ')
                command=s.getmy_audio()
                command=command.lower()
                p.typewrite(command)
                s.speak("Its written")
            if 'close' in command:
                os.system("TASKKILL /F /IM notepad.exe")

             #activate bot   
        elif 'bot' in command:
            flag=College_Opening.database()
            if(flag!=True):
                College_Opening.opening()
            else:
                s.speak("You can do your work")

        #open google 
        elif 'google' in command:
            s.speak("What do you want search")
            search=s.getmy_audio()
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)
            s.speak("Opening your search")

            #ex:- where is south korea  
        elif 'where is' in command:
                location=command.replace('where is','')
                s.speak('getting the location of ' + location)
                webbrowser.open('https://www.google.co.in/maps/place/' + location)
                    
            
             #play music or stop music
        elif command in music:
            music_dir='C:\\Users\\N Ravi Teja\\Music'
            songs=(os.listdir(music_dir))
            flag=True
            if 'stop' in command:
                s.speak("Stopping music")
                os.system("TASKKILL /F /IM Music.UI.exe")
                flag=False
            while(flag):
                num=random.randint(0,len(songs)-1)
                if(songs[num].endswith('.mp3')):
                    os.startfile(os.path.join(music_dir,songs[num]))
                    s.speak("Playing music for you....")
                    flag=False
                
                    
             #ex:- about black hole in wikipedia.           
        elif 'wikipedia' in command:
            s.speak("Searching for the query")
            command=command.replace('wikipedia',"")
            results=wikipedia.summary(command,sentences=2) #sentence=no of lines
            s.speak("according to wikipedia "+results)

            #ex:- open facebook
        elif  'facebook' in command:
            s.speak('opening facebook')
            webbrowser.open_new('www.facebook.com')

            #whats battery level
        elif 'battery' in command:
            s.speak("Getting battery info")
            Battery_CPU.battery()
                
        elif 'news' in command:
            News.News()

        elif 'shutdown' in command:
            os.system('shutdown -s')

        elif 'movie' in command:
            dd.drowsiness_activator()


        elif 'send mail' in command:
            mail=command
            if '@' in mail:
                mail=mail.replace('send mail to',' ')
                Gmail.mail_validation(mail)
            elif 'gmail' in mail:
                mail=mail.replace('send mail to',' ')
                Gmail.mail_validation(mail)
            else:
                last_word=mail.split()
                Gmail.mail_validation(last_word[-1])


        elif 'mail' in command:
            if 'delete all' in command:
                Database_Email.delete_all_email_data()
            elif 'add mail' in command:
                Database_Email.insert_emailid()
        
            elif 'update mail name' in command:
                Database_Email.update_email_nick_name()

            elif 'update mail id' in command:
                Database_Email.update_email_id()
            
            elif 'update mail id' in command:
                Database_Email.delete_email_data()
            
            else:
                s.speak("there is no realted things with mail")

        
        elif 'class database' in command:
            s.speak("what do you want to manipulate in database")
            get=s.getmy_audio()

            if 'add class' in get:
                Database_Class.insert_class_timings()

            elif 'delete all' in get:
                Database_Class.delete_all_class_data()
            
            elif 'delete' in get:
                Database_Class.delete_email_data()
            
            else:
                s.speak("there is no such command in class database")


                
        elif 'screenshot' in command:
                s.speak('what name is should save sir')
                save=s.getmy_audio()
                p.screenshot('C:\\Users\\N Ravi Teja\\Pictures\\Screenshots\\'  +save+ '.png')
                s.speak('taking shot of it sir')
                s.speak('screen shot has done')
                os.startfile('C:\\Users\\POOJA\\Pictures\\Screenshots\\'  +save+ '.png')
                    
        elif 'alarm' in command:
            command=command.split()
            get=command[-2]
            if '.' in get:
                get=get.split('.')
                div=pow(10,len(get[1]))
                timer=(int(get[0])*60)
                timer+=(int(get[1])*60)/div
                timer=int(timer)
            else:
                timer=int(get)*60
                s.speak("Have a nice rest")
                os.startfile('audio_547ebbf828.mp3')
                s.speak(f"alarm for {timer/60} minutes")
                time.sleep(timer)
                os.system('TASKILLL /F /IM Music.UI.exe')
                playsound('best_wakeup_alarm.mp3')
                notification.notify(title="Alarm",message=str(command[-2])+"min completed now Wake Up",timeout=3)
                
        elif 'stop' in command:
            s.speak("Ok sir have a nice day")
            s.speak("Signing off")
            sys.exit()

        elif 'joke' in command:
            s.speak(pyjokes.get_joke())
            s.speak("hehehehehehe")
                
        elif 'distance' in command:
            geocoder=Nominatim(user_agent="capstone project")
            s.speak("which two locations distance you want?")
            s.speak("Say first location")
            location1=s.getmy_audio()
            s.speak("tell second location")
            location2=s.getmy_audio()
            coordinates1=geocoder.geocode(location1)
            coordinates2=geocoder.geocode(location2)
            lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
            lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
            place1=(lat1,long1)
            place2=(lat2,long2)
            dis=distance.distance(place1,place2)
            s.speak("the distance between "+str(location1)+" and "+str(location2)+" is{:.2f}".format(dis))      
                
        else:
            s.speak("I did not understand what you said , tell me again")


if __name__=='__main__':
    maintasks()