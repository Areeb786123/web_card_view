import pyttsx3
import speech_recognition as sr
import webbrowser

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

if __name__ == "__main__":
   speak("hello my name is zara and how may i help you")

sr.Microphone(device_index=1)

r=sr.Recognizer()



r.energy_threeshold=5000

with sr.Microphone() as source:
   print("Speak!")
   audio=r.listen(source)
   try:
      text=r.recognize_google(audio)
      print("You said:".format(text))
      url='https://www.google.com/search?q='
      search_url=url+text
      webbrowser.open(search_url)
   except:
      print("Can't recognize")
