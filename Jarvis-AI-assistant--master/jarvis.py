# JARVIS my AI Assistant

from email import message
from os import name
from posixpath import normcase
import pyttsx3 # 1:pip install pyttsx3 (helps to convert text command to speech.)

import datetime # 2:inbuilt module , which lets us to tell the exact date,time of the system

import speech_recognition as sr#3:  (this helps in taking the command from the user, and recognize the voice through microphone,converts speec to text from the microphone)
# for pyaudio if it does not install , do this:
#     pip install pipwin
#     pipwin install Pyaudio
#     download pyaduio file from outside the source and paste in windows powershell.
import smtplib #4:imported this built-in library to send emails using voice.
from secrets import senderemail,emailpass,to #5:for email creditentials we have added from the seperate file.
from email.message import EmailMessage, Message  #6:from module email.message importing the EmailMessage.
import pyautogui#7: for sending whatsapp message installing package pyautogui
import webbrowser as wb #8: using web browser as we are using whatsapp web.
from time import sleep #9:using this we can stop the screen after a specific time
import wikipedia#10: pip install wikipedia for getting all the data from the wikipedia
import pywhatkit #11: pip install pywhatkit , library for the youtube videos.
import requests #12:pre installled library. for wheather functioning in the jarvis.
#13:News Headline Feature needed to be added later.
import clipboard#14:pip install clipboard. this helps in reading the slected text on the computer.
import os #14:importing os library for openig the vs code using the VS Code.
import pyjokes#15:pip install pyjokes. this will help us to get randiom jokes.
import time as tt #16:for taking the screenshot with exact date and time.
#17: importing string and random for random password genertor.
import string
import random

engine = pyttsx3.init() # declaring engine as variable, init() will call the initial function of the library i.e pyttsx3


#FUNCTION 1: creating a speak function 
def speak(audio):
    engine.say(audio) # enigne.say a predefined function that will convert say function of text to speech

    engine.runAndWait() #runandwait lets the user to speak and wait for the response
    


#FUNCTION 2:creating function to get voices from the comnputer
def getvoices(voice):
    voices= engine.getProperty('voices') #this property lets us  get the voices available in the system.
    # print(voices[1].id)
    if voice==1:
        engine.setProperty('voice',voices[0].id) #for male voice
        speak("hello this is jarvis, How may I help you? ")

    if voice==2:
        engine.setProperty('voice',voices[1].id) #for female voice
        speak("hello this is Friday, How may I help you?")

    
    # while True:
    #     voices=int(input("press 1 for male voice\n Press 2 for female voice\n"))
        
    #     getvoices(voice)


#FUNCTION 3:creating a  time function
def time():
    # I = hour ; M= minutes ; S = seconds 
    Time = datetime.datetime.now().strftime("%I:%M:%S") #converting the datetime to string and assinging the values as hours , minutes and seconds respectively.
    speak(Time)


# FUNCTION 4:creating a function to get the date 
def date():
    year = int(datetime.datetime.now().year) #converts the year in the integer format using the funtion .now
    month = int(datetime.datetime.now().month)# for month
    date = int(datetime.datetime.now().day)#for year
    speak(date)
    speak(month)
    speak(year)

# FUNCTION 5:creating a whisme a function 
def wishme():
    speak("Welcome back , glad to  see you coming back")
    speak("The current time is")
    time()#speaks the time function
    speak("The Current date is")
    date()#speaks the date function

#creating a greeting function
    # for wishme command , we decalre a variable hour and created a nest if else statement to fulfill our condition.
    hour =  datetime.datetime.now().hour
    if hour >= 6 and hour<12: #from 6am to 12pm
        speak("Good Morning!")
    elif hour>=12  and hour<18: #from 12pm to 6pm
        speak("Good afternoon")
    elif hour >=18 and hour<24: #from 6pm to 12am
        speak("Good evening")
    else:
        speak("Good night") #after 12am

    speak("Now I JARVIS is  at your service , Please tell me how may I help you?")

# wishme()


# ************takecommand() in  2 types*****************

#FUNCTION 6.1:defining function to take command in cmd :this will help is to ask in command line
def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

#FUNCTION 6.2: defing function for taking the command through microphone
def takecommandMIC():

    r =sr.Recognizer() #declaring r as another variable,and recognizer function is used for voice recognition
    with sr.Microphone() as source: #setting the microphone as a source
        print("Listening.....")
        r.pause_threshold = 1 #this let the jarvis to listen for 1 sec
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN") #setting the language to indian english and recognizing as google voice. 
        print(query)
        
    # Exception case if not recognized 
    except Exception as e:
        print(e)
        speak("Say that again please")#if ai is unable to catch the command
        return "None"
    return query


#FUNCTION 7: creating a function to send emails using voice.
def sendEmail(receiver, subject ,content):
    server = smtplib.SMTP('smtp.gmail.com',587) #setting the server to smtp gmail so that it can recognize.
    server.starttls() #startttls :transport layer security whic creates secure network to send emails.
    server.login(senderemail,emailpass)
    email = EmailMessage()
    email['From'] = sendEmail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close() #for loging out of the server securely.

#FUNCTION 8: creating a function to send whatsapp message using voice.
def sendwhatsappmsg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

#FUNCTION 9: creating a function to search on google with voice.
def searchgoogle():
    speak("What should I search for?")
    search = takecommandMIC()
    wb.open('https://www.google.com/search?q='+search)

#Function 11: creating a function to speak the text highlighted by the user.
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


#FUNCTION 12: Covid-19 updates function.
def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    covid_data = f'confirmwd cases: {data["cases"]} \n Deaths:{data["deaths"]} \n Recovered Cases:{data["recovered"]}'
    print(covid_data)
    speak(covid_data)

#FUNCTION 13: Screen Shot function that will take ss using voice command.
def screen_shot():
    name_img = tt.time()#this will give current datetime of the image taken.
    name_img = f'D:\\Python\\Python Projects\\Jarvis\\ScreenShots\\{name_img}.png'#setting up the path for the screenshhots to be saved.
    img = pyautogui.screenshot(name_img)#for taking screenshot.
    img.show()#this will open the image for us.

#FUNCTION 14: Random Password generator function created.
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation


    passlen = 8
    s= []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

#FUNCTION 15: Creating a flip coin function.
def flip():
    speak("Okay sir, Flippping a coin")
    coin =['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss =  ("".join(toss[0]))
    speak("I flipped the coin and you got"+toss)

#FUNCTION 16:Creating a roll dice function.
def roll():
    speak("Okay Sir,Rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I rolled a die and you got"+roll)


 #sytnax to write main function in python
if __name__ == "__main__":
            getvoices(1) #this will help the changing the voice from male and female
    # wishme()
while True:
        #.lower converts all the text to lowercase
        query = takecommandMIC().lower()
        # if the user write time in the query than we will be printing the time by calling the function 
        if 'time' in query:
            time()
        # if the user write date in the query than we will be printing the date by calling the function
        elif 'date' in query:
            date()
        
        
        
        #Email execution in main function.
        elif 'email' in query:
            # creating a dictionary for the emails.
            email_list = {
                'me':'vkhushboo4921@gmail.com'
            }
            try:
                speak('To whom you want to send the mail')
                name = takecommandMIC() #taking the name from the microphone input.
                receiver = email_list[name] #receiver list will be generated from the dictionary created above.
                speak("What is the subject of the mail")
                subject = takecommandMIC()
                speak('What should I say?')
                content = takecommandMIC()
                sendEmail(receiver, subject ,content)
                speak('email has been send')

            except Exception as e:
                print(e)
                speak("unable to send the email")

        
        # whatsapp message execution.
        elif 'message' in query:
            user_name={ #dictionary created for storing numbers.
                'me':'+91 9015701705',
                
            }
            try:
                speak('To whom you want to send the whats app message?')
                name = takecommandMIC() #taking the name from the microphone input.
                phone_no = user_name[name] #receiver list will be generated from the dictionary created above.
                speak("What is the message?")
                message = takecommandMIC()
                sendwhatsappmsg(phone_no,message)
                speak("Message has been sent")
            
            except Exception as e:
                print(e)
                speak("unable to send the message")
        
        #wikipedia execution
        elif 'wikipedia' in query:
            speak("searching on wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences =4)
            print(result)
            speak(result)

        #google searching execution.
        elif 'google search' in query:
            searchgoogle()

        #youtube searching execution.
        elif 'youtube' in query:
            speak("What should I search for on Youtube?")
            topic = takecommandMIC()
            pywhatkit.playonyt(topic)
        
        #weather execution.
        elif 'weather' in query:
            city = 'new York'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e20c3c8258a7c526ac5d4658b88ec056"
            
            
            res = requests.get(url)
            data = res.json()
            
            weather = data['weather'] [0] ['main']
            temperature = data['main'] ['temp']
            description = data['weather'] [0] ['description']
            temperature = round((temperature - 32) * 5/9) #converted farenheit to degree celsius. round used because we don't need data in the form of floating point numbers.
            
            print(weather)
            print(temperature)
            print(description)
            speak(f'weather in {city} city is like')
            speak('temperature : {} degree celcius'.format(temperature))
            speak('weather is {}'.format(description))

        #reading text to speech execution.
        elif 'read' in query:
            text2speech()

        #Covid-19 execution.
        elif 'covid' in query:
            covid()
        #to open My Documents using the voice command.
        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        #for opening the VS code usig the voice command.
        elif 'code' in query:
            codepath = '""C:\Users\hp\Downloads\VSCodeUserSetup-x64-1.69.2.exe""'
            os.startfile(codepath)

        #for opening the Microsoftword usig the voice command.
        elif 'word' in query:
            codepath = '"C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"'
            os.startfile(codepath)

        #for opening illustrator using voice command.
        elif 'illustrator' in query:
            codepath = '"D:\\Adobe\\Adobe_Illustrator_CC_2019\\Adobe Illustrator CC 2019\\Support Files\\Contents\\Windows"'
            os.startfile(codepath)

        #Jokes execution .
        elif 'joke' in query:
            j=pyjokes.get_jokes
            speak(j)

        #ScreenShot Function Execution.
        elif 'screenshot' in query:
            screen_shot()
        
        #remeber execution.
        elif 'remeber that' in query:
            speak("What should I remeber")
            data = takecommandMIC()
            speak("You said me to remember that"+data)
            remember = open('data.txt','w')#jarivs will be storing the data in a txt file which he will read once asked by the user.
            remember.write(data)
            remember.close()
        elif 'do you know annything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember that"+remember.read())

        #Random pass generator function execution.
        elif 'pass' in query:
            passwordgen()

        #Coin toss Function execution.
        elif 'flip' in query:
            flip()

        #roll die execution.
        elif 'roll' in query:
            roll()

        #to quit form the loop.
        elif 'offline' in query:
            quit()

