import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from selenium import webdriver
import smtplib
import pywhatkit
import psutil
import requests, json
from translate import Translator
import random
import PyPDF2
import winsound
import pyautogui
import operator
import time
import pandas as pd
import cv2
from plyer import notification
import threading


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def alarms(Timing):
		altime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
		altime=altime[11:-3]
		horeal=altime[:2]
		horeal=int(horeal)
		mireal=altime[3:5]
		mireal=int(mireal)
		while True:
			if horeal==datetime.datetime.now().hour:
				if mireal==datetime.datetime.now().minute:
					winsound.PlaySound("abc",winsound.SND_LOOP) 
				elif mireal<datetime.datetime.now().minute:
					break

def speak(audio):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-2)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Victoria")
    time.sleep(0.1)
    speak("Please tell me how may I help you sir?")       
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.energy_threshold=200
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('epsilonraj1947@gmail.com', 'G@879@879@')
    server.sendmail('epsilonraj1947@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'timer for whatsapp message' in query:
            try:
                speak("tell me name Whom you want to send the message")
                a=takeCommand().lower()
                df=pd.read_csv('school.csv')
                cf=df.loc[:,["number"]]
                cf.index=df["name"].values
                ef=cf.loc[[a],["number"]]
                to=ef["number"].values
                to=str(to)
                res = "".join(('+', to))
                a=res.replace("[", '')
                z=a.replace("]", '')
                speak("target locked")
                try:
                    speak("what do you want to send")
                    b=takeCommand()
                    try:
                        speak("time when you want to send the message")
                        y=takeCommand()
                        c=str(y)
                        k=c.index(":")
                        r=c[k-1::-1]
                        e=r[::-1]
                        d=c[k+1:k+3:1]
                        g=int(e)
                        h=int(d)
                        
                        if "p.m" in y:
                            g=g+12
                            pywhatkit.sendwhatmsg(z,b,g,h)
                        else:
                            pywhatkit.sendwhatmsg(z,b,g,h)
                    except Exception as e:
                        print(e)
                        speak("faild try again")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")  
            except Exception as e:
                    print(e)
                    speak("Sorry sir")
        elif 'open youtube' in query:
            speak("sure")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("sure")
            webbrowser.open("google.com")
        elif 'facebook' in query:
            speak("sure")
            webbrowser.open("https://www.facebook.com/")
        elif 'instragram' in query:
            speak("ok")
            webbrowser.open("https://www.instagram.com/")
        elif 'open stackoverflow' in query:
            speak("sure")
            webbrowser.open("stackoverflow.com") 
        elif 'open i l i' in query:
            speak("sure")
            webbrowser.open("https://ilizone.iul.ac.in/login/index.php")  
        elif 'play song' in query:
            try:
                speak("Which type of song should I play?")
                content = takeCommand()
                speak("playing")
                if 'audio' in content:
                     a=random.randint(1,len('D:\\favorit')+1)
                     music_dir = 'D:\\favorit'
                     songs = os.listdir(music_dir)
                     os.startfile(os.path.join(music_dir, songs[a]))
                elif 'video' in content:
                     a=random.randint(1,len('D:\\video')+1)
                     music_dir = 'D:\\video'
                     songs = os.listdir(music_dir)    
                     os.startfile(os.path.join(music_dir, songs[a]))
                else:
                     speak('this type of song not avlable')
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'excel' in query:
            speak("ok sir")
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
        elif 'open vlc' in query:
            speak("sure")
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"    
            os.startfile(codePath)
        elif 'send mail' in query:
            try:
                speak("password please")
                q=takeCommand().lower()
                if "879" in q:
                    try:
                        speak("Whom you want to send mail")
                        a = takeCommand().lower()
                        df=pd.read_csv('school.csv')
                        cf=df.loc[:,["email"]]
                        cf.index=df["name"].values
                        ef=cf.loc[[a],["email"]]
                        to=ef["email"].values
                        speak("target locked")
                        try:
                            print(to)
                            print(a)
                            speak("What should I say?")
                            content = takeCommand()
                            speak("copy that")
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir. I am not able to send this email")  
                    except Exception as e:
                            print(e)
                            speak("information not found")  
                else:
                    speak("wrong password")
            except Exception as e:
                speak("faild try again")
        elif "who are you" in query:
                    speak("my name is sara")
        elif "who makes you" in query:
                    speak("mister Raj ")
        elif "how are you" in query:
                    speak("pretty good ")
        elif "i love you" in query:
                    speak("wow this is the best moment for me till date but i can't love you becouse i am a  robot")
        elif "it's pleasure to meet you" in query:
                    speak("me too sir")
        elif " i hate you " in query:
                    speak("wow , i hate me too we should be friends ")
        elif "good morning" in query:
                    speak("good morning sir")
        elif "good evening" in query:
                    speak("good evening sir")
        elif query=="sara":
                    speak("yes sir")     
        elif 'binary to decimal' in query:
            try:
                speak("tell me the binary number")
                content = takeCommand()
                speak("converting")
                sum=0
                for i in range(len(content)):
                    b=int(content[i])*(2**(len(content)-i-1))
                    sum=sum+b
                speak("decimal number is")
                print(sum)
                speak(sum)
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to understand")
        elif 'decimal to binary' in query:
            try:
                speak("tell me the decimal number")
                content = takeCommand()
                content=int(content)
                speak("converting")
                z=[]
                def bino(content):
                    while int(content)>2:
                        b=content%2
                        z.append(b)
                        content=content//2
                    z.append(content)
                    speak("binary number is")                                                                              
                    print(z[-1::-1])
                    speak((z[-1::-1]))
                bino(content)
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to understand")
        elif 'play' in query:
                speak("target locked")
                pywhatkit.playonyt(query)
                time.sleep(4)
                pyautogui.press("f")
        elif 'close chrome' in query:
                os.system("taskkill /f /im msedge.exe")
                os.system("taskkill /f /im chrome.exe")
                speak("target has been destroyed")
        elif 'close vlc' in query:
                os.system("taskkill /f /im vlc.exe")
                speak("target has been destroyed")
        elif 'close excel' in query:
                os.system("taskkill /f /im excel.exe")
                speak("target has been destroyed")
        elif 'close vs studio' in query:
                os.system("taskkill /f /im code.exe") 
                speak("target has been destroyed")       
        elif "shutdown computer" in query:
                os.system("taskkill /f /im vlc.exe")
                os.system("taskkill /f /im excel.exe")
                os.system("taskkill /f /im msedge.exe")
                os.system("taskkill /f /im chrome.exe")
                os.system("shutdown /s /t 10")
        elif "restart computer" in query:
                os.system("taskkill /f /im vlc.exe")
                os.system("taskkill /f /im excel.exe")
                os.system("taskkill /f /im msedge.exe")
                os.system("taskkill /f /im chrome.exe")
                os.system("shutdown /r /t 10")   
        elif 'whatsapp message' in query:
            try:
                speak("password please")
                q=takeCommand().lower()
                if "879" in q:
                    try:
                        speak("tell me name Whom you want to send the message")
                        a=takeCommand().lower()
                        df=pd.read_csv('school.csv')
                        cf=df.loc[:,["number"]]
                        cf.index=df["name"].values
                        ef=cf.loc[[a],["number"]]
                        to=ef["number"].values
                        to=str(to)
                        res = "".join(('+', to))
                        a=res.replace("[", '')
                        z=a.replace("]", '')
                        speak("target locked")
                        try:
                            speak("what do you want to send")
                            b=takeCommand()
                            speak("copy that")
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            c=str(strTime)
                            if (int(c[6:8])>38):
                                d=int(c[:2])
                                e=int(c[3:5])+2 
                                pywhatkit.sendwhatmsg(z,b,d,e)
                            else:
                                d=int(c[:2])
                                e=int(c[3:5])+1
                                pywhatkit.sendwhatmsg(z,b,d,e)
                        except Exception as e:
                            print(e)
                            speak("faild try again")
                    except Exception as e:
                        speak("information not found")
                else:
                    speak("wrong password try again")
            except Exception as e:
                print(e)
                speak("faild") 
        elif "alarm" in query:
            speak("sir please tell me time to set alarm")
            alarm=takeCommand()
            speak("alarm has been set")
            alarm=alarm.replace("set alarm to","")
            alarm=alarm.replace(".","")
            alarm=alarm.upper()
            alarms(alarm)
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "calculate" in query:
            query=query.replace("sara calculate","")
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    'Mod' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                 op1,op2 = int(op1), int(op2)
                 return get_operator_fn(oper)(op1, op2)
            speak(eval_binary_expr(*(query.split())))
        elif "bomb" in query:
            speak("what should i say")
            a=takeCommand()
            try:
                speak("how meany times bombing do you want ")
                b=takeCommand()
                speak("copy that")
                f=int(b)
                i=0
                while i<f:
                   pyautogui.typewrite(a)
                   pyautogui.press("enter")
                   i=i+1
            except Exception as e:
                   print(e)
                   speak("Sorry sir")
        elif "attendance" in query:
            speak("ok sir")
            webbrowser.open("https://ilizone.iul.ac.in/my/")
            time.sleep(10)
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(10)
            hour = int(datetime.datetime.now().hour)
            x = datetime.datetime.now()
            y=x.strftime("%a")
            if (y=="Mon") or (y=="Wed") or (y=="Fri"):
                if 21>=hour>=11:
                    for i in range(1,13):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,21):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,26):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,19):
                        pyautogui.press("tab")
                    pyautogui.press("down")   
                    pyautogui.press("up")
                    pyautogui.press("enter")
                    time.sleep(7)
                    os.system("taskkill /f /im msedge.exe") 
                    speak("mission succeed")
                elif 11>hour>=10:
                    for i in range(1,39):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,79):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(15)
                    for i in range(1,21):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,26):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,19):
                        pyautogui.press("tab")
                    pyautogui.press("down")   
                    pyautogui.press("up")
                    pyautogui.press("enter")
                    time.sleep(7)
                    os.system("taskkill /f /im msedge.exe") 
                    speak("mission succeed")
            else:
                if 10>=hour>=9:
                    for i in range(1,25):
                        pyautogui.press("tab")                         
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,21):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,26):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,19):
                        pyautogui.press("tab")
                    pyautogui.press("down")   
                    pyautogui.press("up")
                    pyautogui.press("enter") 
                    time.sleep(10)
                    os.system("taskkill /f /im msedge.exe")
                    speak("mission succeed")
                elif 12>=hour>=11:
                    for i in range(1,31):
                        pyautogui.press("tab")                          
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,15):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,20):
                        pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(10)
                    for i in range(1,13):
                        pyautogui.press("tab")
                    pyautogui.press("down")   
                    pyautogui.press("up")
                    pyautogui.press("enter")
                    time.sleep(7)
                    os.system("taskkill /f /im msedge.exe")   
                    speak("mission succeed")
        elif "weather in" in query:
                z=query.index("in")
                CITY =query[z+2::]
                API_KEY = "e6e860d956390f4a7a4176a72d6f8f2c"
                URL = "https://api.openweathermap.org/data/2.5/weather?q="+CITY+"&appid="+API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                     data = response.json()
                     main = data['main']
                     temperature = round(main['temp']-273.15)
                     t=str(temperature)
                     te=t.replace("°C","")
                     temp=int(te)
                     humidity = main['humidity']
                     pressure = main['pressure']
                     report = data['weather']
                     report = data['weather']
                     speak(f"{CITY:-^30}")
                     speak(f"Temperature: {temperature} degree Celcius  ")
                     speak(f"Humidity: {humidity}")
                     speak(f"Pressure: {pressure}")
                     speak(f"Weather Report: {report[0]['description']}")
                     wet=str(report[0]['description'])        
        elif "weather" in query:
                CITY = "Lucknow"
                API_KEY = "e6e860d956390f4a7a4176a72d6f8f2c"
                URL = "https://api.openweathermap.org/data/2.5/weather?q="+CITY+"&appid="+API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                     data = response.json()
                     main = data['main']
                     temperature = round(main['temp']-273.15)
                     t=str(temperature)
                     te=t.replace("°C","")
                     temp=int(te)
                     humidity = main['humidity']
                     pressure = main['pressure']
                     report = data['weather']
                     report = data['weather']
                     #speak(f"{CITY:-^30}")
                     speak("weather of lucknow is")
                     speak(f"Temperature: {temperature} degree Celcius  ")
                     speak(f"Humidity: {humidity}")
                     speak(f"Pressure: {pressure}")
                     speak(f"Weather Report: {report[0]['description']}")
                     wet=str(report[0]['description'])
                     if "rain" in wet:
                        speak("sir the possibility of rain seems to be there today ,if you Are thinking of going out ,then please take umbrella with you")
                     elif "snow" in wet or temp<=15:
                        speak("sir it's cold day outside ,if you Are thinking of going out ,then please take jacket or blanket with you")
                     elif temp>=38 and wet=="clear sky":
                        speak("sir the temperature is high outside ,if you Are thinking of going out ,then please take sunglasses and umbrella with you")
                else:
                     speak("Error in the HTTP request") 
        elif "covid report" in query:
                    covidData = None
                    try:
                        covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
                    except:
                        print("Please! Check your internet connection")
                    if (covidData != None):
                        data = covidData.json()['Success']
                        notification.notify(
                                title = "COVID19 Stats on {}".format(datetime.date.today()),
                                message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                                            totalcases = data['cases'],
                                            todaycases = data['todayCases'],
                                            todaydeaths = data['todayDeaths'],
                                            active = data["active"]),  
                                timeout  = 25                               
                        )
                        time.sleep(1)
                        totalcases = data['cases']
                        todaycases = data['todayCases']
                        todaydeaths = data['todayDeaths']
                        active = data["active"]
                        speak("covid report of india is")
                        speak(f"totalcases: {totalcases}")
                        speak(f"todaycases: {todaycases}")
                        speak(f"todaydeaths: {todaydeaths}")
                        speak(f"active: {active}")
        elif "watch over" in query:
            status_list=[None,None]

            alarm_sound = pyttsx3.init()
            voices = alarm_sound.getProperty('voices')
            alarm_sound.setProperty('voice', voices[0].id)
            alarm_sound.setProperty('rate', 150)

            def voice_alarm(alarm_sound):
                i=0
                while i<6:
                    
                    alarm_sound.say("Object Detected")
                    alarm_sound.runAndWait()
                    i+=1


            video=cv2.VideoCapture(0)
            initial_frame = None

            while True:
                check, frame = video.read()
                frame = cv2.flip(frame,1)
                status=0

                gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                gray_frame=cv2.GaussianBlur(gray_frame,(25,25),0)

                blur_frame = cv2.blur(gray_frame, (5,5))
                
                if initial_frame is None:
                    initial_frame = blur_frame
                    continue

                delta_frame=cv2.absdiff(initial_frame,blur_frame)
                threshold_frame=cv2.threshold(delta_frame,35,255, cv2.THRESH_BINARY)[1]

                (contours,_)=cv2.findContours(threshold_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


                for c in contours:
                    if cv2.contourArea(c) <500:
                        continue
                    status=status + 1
                    (x, y, w, h)=cv2.boundingRect(c)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)
                status_list.append(status)

                if status_list[-1]>= 1 and status_list[-2]==0:
                    alarm = threading.Thread(target=voice_alarm, args=(alarm_sound,))
                    alarm.start()

                cv2.imshow('motion detector', frame)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break

            alarm_sound.stop()
            video.release()
            cv2.destroyAllWindows()                               