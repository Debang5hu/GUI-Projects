#!/usr/bin/python3

# _*_ coding:utf-8 _*_

# NOTE: to add
# date & time [done]
# response to hello [done]
# searching web for gathering information  [done]


# kudos: https://stackoverflow.com/questions/57751564/pyttsx3-voice-gender-female


import pyttsx3 #type: ignore
import speech_recognition as sr #type: ignore
import datetime
from fetchinfo import weather,headlines,info  # custom module
from sys import exit

name = 'zara'

class zaraf():
    def __init__(self):
        self.zara = pyttsx3.init()
        
        # for linux
        self.zara.setProperty('voice', 'english_rp+f3')   # female voice
        self.zara.setProperty('rate', 170)

        # setting up for speech input
        self.recognizer=sr.Recognizer()


    # for voice output [dry implemented]
    def speak(self,text):
        self.zara.say(text)
        self.zara.runAndWait()


    def response(self,words):
        if name in words:
            words = words.replace(name,'')

            if 'hi' in words or 'hello' in words:
                zara.speak('hey how can i help you')
            
            # greet
            if 'morning' in words:
                zara.speak('good morning')
            if 'afternoon' in words:
                zara.speak('good afternoon')
            if 'night' in words:
                zara.speak('good night')

            # time
            if 'time' in words:
                time = datetime.datetime.now().strftime('%I %M  %p')
                zara.speak(f'Current time is {time}')

            # date
            if 'date' in words:
                date = datetime.date.today().strftime("%d %B %Y")
                zara.speak(f'Today is {date}')

            if 'weather' in words:
                zara.speak(weather())
            
            # general knowledge
            if 'tell me' in words and 'about' in words:
                words = words.replace('tell me','')
                words = words.replace('about','')
                zara.speak(info(words))

            # top 5 headlines
            if 'headline' in words:
                words = words.replace('headline','')
                res = headlines()
                for x in range(len(res)):
                    print(res[x])
                    zara.speak(res[x])

            
            # for quitting
            if 'bye' in words:
                zara.speak('Sayonara')
                exit()
        else:
            pass

    def listen(self):
        try:
            with sr.Microphone() as mic:
                self.recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = self.recognizer.listen(mic)
                
                try:
                    text = self.recognizer.recognize_google(audio).lower()   # lowercase
                    print(text)
                    return text
                except sr.UnknownValueError():
                    print('unknown value')
                except sr.RequestError():
                    print('request error')
                except:
                    return None
        
        except KeyboardInterrupt:
            pass

        except:
            zara.speak('mic not found')
            return None
            sys.exit()


        '''text = input('enter: ')
        return text'''




if __name__  == '__main__':
    zara = zaraf()
    while True:    
        command = zara.listen().lower()
        if command:
            zara.response(command)
