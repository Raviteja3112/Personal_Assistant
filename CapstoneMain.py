from datetime import datetime
from playsound import playsound
import sys
import time
from PyQt5 import  QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from JarvisUI import Ui_MainWindow
import Speak as s
import MainTasks
import Battery_CPU
import News

def ProgramStarting():
    now=datetime.now()
    hour=int(now.strftime("%H"))
    if hour<=12:
        s.speak("Good Morning..")
    elif hour>=13 and hour<=17:
        s.speak("Good Afternoon...")
    else:
        s.speak("Good Evening...")

    time.sleep(1)
    s.speak("Getting all system drivers")
    now=datetime.now().strftime("%d %b %y")
    s.speak("Today's date is "+now)
    time.sleep(1)
    Battery_CPU.battery()
    Battery_CPU.cpu_usage()
    time.sleep(1)
    s.speak("Todays news is:")
    News.News()
    s.speak("News Over...")
    s.speak("Ready to do main tasks")
    MainTasks.maintasks()


class Main(QMainWindow):
    def __init__(self):
        playsound('Startup Sound.mp3')
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:\\Users\\N Ravi Teja\\Downloads\\Codes\\BoringTerribleDutchshepherddog-small.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        ProgramStarting()


app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())

