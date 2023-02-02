#External Imports
import pyttsx3


### Getting Properties
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')



### Setting Properties
engine.setProperty('rate', rate-35)
engine.setProperty('volume', volume-0.25)
voice_id = voices[1].id
engine.setProperty('voice', voice_id)



def speak(str):
   engine.say(str)
   engine.runAndWait()


# if __name__ == "__main__":
#    for voice in voices:
#       engine.setProperty('voice', voice.id)
#       print(f"{voice.id}")
#       engine.say('The quick brown fox jumped over the lazy dog.')
#    engine.runAndWait()