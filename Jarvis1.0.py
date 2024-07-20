import pyttsx3
import datetime
import speech_recognition as sr 
import smtplib
import pyautogui
import webbrowser 
from time import sleep
import wikipedia
import pywhatkit
import clipboard
import requests
import pyjokes
import time as tt
import random
import string
import psutil
import os
from googletrans import Translator, constants
from pprint import pprint
from translate import Translator


engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices():
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voices == 1:
        engine.setProperty('voice', voices[0].id)

    if voices == 2:
        engine.setProperty('voice', voices[1].id)

    speak("Hello This is Jarvis")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour<12:
        speak("good morning sir i am virtual assistent jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am virtual assistent jarvis") 
    else:
        speak("good night sir i am virtual assistent jarvis")

def wishme():
    speak("Hello Sir")
    greeting()
    #time()
    #date()
    speak("I am ready sir")
    
# def takeCommandCmd():
#     query = input("Pls tell Me How Can I Help You\n")
#     return query


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising.") 
        query = r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e :                #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jsjdob2002@gmail.com', 'bruce is great')
    server.sendmail('jsjdob2002@gmail.com', to, content)
    server.close()

def sendwhatmssg(phone_no, message):
    Message = message
    webbrowser.open('https://web.whatsapp.com/send?phone'+phone_no+'&text'+Message)
    sleep(30)
    pyautogui.press('enter')
    
def searchgoo():
    speak("What should I search for?")
    search = takecom()
    webbrowser.open('https://www.google.com/search?q='+search)

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def takenote():
    note = takecom()
    note='\n'+note+' '+"{:%B %d, %Y}".format(datetime.now())
    file=open('notes.txt','a')
    file.write(note)

def tellnote():
    speak(' sir for what date you want the note for ?')
    date = takecom()
    file = open('notes.txt','r')
    notetoken=0
    for i in file:
        if date in i:
            notetoken = 1
            speak(i)
            break
    if notetoken == 0:
        speak('sorry sir , no notes found for the given date ')

def covid():
    r = requests.get('https://coronavirus-19-api-herokuapp.com/all')

    data = r.json()
    covid_data = f'Confrimed cases : {data["cases"]} \n Deaths : {data["deaths"]}  \n Recovered {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'F:\\Jarvis\\screenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def flip():
    speak("Ok sir Flipping A Coin")
    coin = ['Heads', 'Tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print("I Flipped the Coin and you got"+toss)
    speak("I Flipped the Coin and you got"+toss)

def roll():
    speak("Ok sir Rolling A Die")
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print("I Rolled A Die and you got\n"+roll)
    speak("I Rolled A Die and you got\n"+roll)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at\n" + usage + "Percent")
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)
    speak("Percent")

def trans():
    from googletrans import Translator, constants
    from pprint import pprint
    from translate import Translator


    # init the Google API translator
    translator= Translator(to_lang="french")

    #Sample Translations
    translation = translator.translate("Good Morning!")
    print(translation)

    # translate more than a phrase
    sentences = [
        "Hello everyone",
        "How are you ?",
        "Do you speak english ?",
        "Good bye!"
    ]

    for x in sentences:
        translation = translator.translate(x)
        print(translation)

speak("enter a password")
val = input("Enter your value: ")
if val=='1234':
    print('opened')

    if __name__ == "__main__" :
        wishme()
    while True:
        query = takecom().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecom()
                to = "jsjdob2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")

        elif 'message' in query:
            user_name = {
                'Jarvis': '+917780565427'
            }
            try:
                speak("To Whom You Want To Send The WhatsApp Mssg?")
                name = takecom()
                phone_no = user_name[name]
                speak("What's the message?")
                message = takecom()
                sendwhatmssg(phone_no, message)
                speak("Message has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry sir i am unable to send the message")  

        elif 'wikipedia' in query:
            speak("Searching On Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2) 
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoo()

        elif 'youtube' in query:
            speak("What can i search for you?")
            topic = takecom()
            pywhatkit.playonyt(topic)

        elif 'read' in query:
            text2speech()

        elif 'covid' in query:
            covid()
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif'screenshot' in query:
            screenshot()

        elif'translate' in query:
            trans()

        elif 'flip' in query:
            flip()

        elif 'roll' in query:
            roll()

        elif 'cpu' in query:
            cpu()
        
        elif 'take notes' in query:
            speak('shure sir , what would you like me to take in note ?')
            takenote()

        elif ' tell note' in query:
            tellnote()

        elif 'exit' in query:
            quit()

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")  

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0])) 

        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
                
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Jai Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hey Jai  ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 

        elif query == 'none':
            continue 

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)        

else:
    speak("Access Denied")
        

         

