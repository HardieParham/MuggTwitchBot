import pyttsx3


"""Getting Properties"""
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')


"""Setting Properties"""
engine.setProperty('rate', rate-20)
engine.setProperty('volume', volume-0.05)
voice_id = voices[1].id
engine.setProperty('voice', voice_id)


def connect() -> bool | Exception:
   if engine is not None:
        return True
   else:
      raise Exception('ModuleFailure')


def speak(str: str) -> None:
   engine.say(str)
   engine.runAndWait()


def set_volume(num: int) -> None:
   new_volume = num/100
   engine.setProperty('volume', new_volume)