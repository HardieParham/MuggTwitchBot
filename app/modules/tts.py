#External Imports
import pyttsx3


### Getting Properties
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')



### Setting Properties
engine.setProperty('rate', rate-15)
engine.setProperty('volume', volume-0.10)
voice_id = voices[1].id
engine.setProperty('voice', voice_id)


def connect():
   if engine is not None:
        return True
   else:
      raise Exception('ModuleFailure')


def speak(str):
   engine.say(str)
   engine.runAndWait()


def set_volume(num):
   new_volume = num/100
   engine.setProperty('volume', new_volume)


# if __name__ == "__main__":
#    for voice in voices:
#       engine.setProperty('voice', voice.id)
#       print(f"{voice.id}")
#       engine.say('The quick brown fox jumped over the lazy dog.')
#    engine.runAndWait()