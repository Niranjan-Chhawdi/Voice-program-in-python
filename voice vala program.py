f = open("voice.txt" , "w")

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    print("Speak AnyThing.....")
    audio = r.listen(source)
    
    try :
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        f.write(text)
    except :
        print("Nahi suna ")

f.close()

