import datetime
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
    wishme()
    while 1:
        query = takecommand().lower()
        # Logic for executing task based on query
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                 ["whatsapp", "https://web"
                              ".whatsapp.com/"], ["mp", "https://mptenders.gov.in/nicgep/app]"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query:
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open instagram' in query:
            speak('Opening Instagram sir...')
            Instabot()

        elif 'time is now' in query:
            strfdTime = datetime.datetime.now().strftime("%H:%M:%S of %d:%m:%Y")
            speak(f"Sir the time is {strfdTime}")


def Temp(self):
    search = "temperature in Jaora"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    speak(f"The Temperature Outside Is {temperature} celcius")

    speak("Do I Have To Tell You Another Place Temperature ?")

    if 'yes' in query:
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
