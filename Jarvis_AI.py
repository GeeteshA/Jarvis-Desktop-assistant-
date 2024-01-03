import datetime
import sys
import webbrowser
import os
import wikipedia
import pyttsx3
import speech_recognition as sr
import requests  # Temprature checker code
from bs4 import BeautifulSoup
from selenium import webdriver  # start of Automation
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IgPassword import Username, Password
from selenium.webdriver.common.by import By
import time  # End
# for Gui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_JarvisUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I Am Jaarvis sir! Please tell me how may I help You?")


class Instabot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        s = Service("D:/selenium/chromedriver.exe")

        driver = webdriver.Chrome(options=options, service=s)

        driver.get("https://instagram.com/")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(Username)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(
            Password)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")))
        element.click()


#
# class Temp:


if __name__ == '__main__':
    class MainThread(QThread):
        def __init__(self):
            super(MainThread, self).__init__()


    def run(self):
        self.TaskExecution()

        def takecommand():
            # It takes microphone input from user and return STRING output
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio)
                print(f"user said: {query}\n")

            except Exception as e:
                print("Say! that again Please...")
                return "None"
            return query

        def Temp():
            search = "temperature in Jaora"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"The Temperature Outside Is {temperature} celcius")

            speak("Do I Have To Tell You Another Place Temperature ?")

            if 'yes' in self.query:
                speak("Tell Me The Name Of tHE Place ")
                name = takecommand()
                search = f"temperature in {name}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temperature = data.find("div", class_="BNeawe").text
                speak(f"The Temperature in {name} is {temperature} celcius")

            else:
                speak("no problem sir")

        def TaskExecution():
            wishme()
            while 1:
                self.query = self.takecommand().lower()
                # Logic for executing task based on query
                sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                         ["whatsapp", "https://web"
                                      ".whatsapp.com/"], ["mp", "https://mptenders.gov.in/nicgep/app]"]]

                for site in sites:
                    if f"Open {site[0]}".lower() in self.query:
                        speak(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])

                if 'wikipedia' in self.query:
                    speak('Searching wikipedia...')
                    query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif 'play music' in self.query:
                    music_dir = 'D:\\Music'
                    songs = os.listdir(music_dir)
                    # print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                elif 'open instagram' in self.query:
                    speak('Opening Instagram sir...')
                    Instabot()

                elif 'time is now' in self.query:
                    strfdTime = datetime.datetime.now().strftime("%H:%M:%S of %d:%m:%Y")
                    speak(f"Sir the time is {strfdTime}")

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Ui/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Ui/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
