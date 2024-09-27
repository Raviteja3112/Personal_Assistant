import pyttsx3
import speech_recognition as sr

voice=pyttsx3.init('sapi5')
def speak(told):
        voices=voice.getProperty('voices')
        voice.setProperty('voice',voices[1].id)
        voice.setProperty('rate',175)
        voice.say(told)
        print(told)
        voice.runAndWait()



def getmy_audio():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0)
                r.pause_threshold=0.7
                speak("I am listening")
                #take input from microphone
                audio=r.listen(source)
                speak("Listen over")
                said=" "
                try:
                        said=r.recognize_google(audio)
                        print(said)
                except Exception as e:
                        print(str(e))
        speak(said)
        return said


if __name__=="__main__":
        command=getmy_audio()
