import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
r=sr.Recognizer()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def  speak(audio):
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

      speak("I am Zaara Please tell how may I help you") 

def takeCommand():
        #It takes microphone input from the user and returns the string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en_in')
                print(f"User said:{query}\n")

        except Exception as e:
                print(e)

                print("Say that again please...")
                return "None"   
        return query 
        
if __name__ == "__main__": 
   speak("Hello Areeb ")    
   wishMe()
   #while True:
   if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if "wikipedia" in query:
           speak("Searching information on Wikipedia.....")
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences=3)
           print("Speaking........\n")
           speak("Sir, According to Wikipedia")
           print(results)
           speak(results) 
        elif "open youtube" in query:
                webbrowser.open("www.youtube.com") 
        elif"open google" in query:
                webbrowser.open("www.google.com")
        elif"open weather forecast" in query:
                webbrowser.open("https://www.accuweather.com/")
        elif"open irctc" in query:
                webbrowser.open("https://www.irctc.co.in/nget/train-search")  
        elif"open yatra" in query:
                webbrowser.open("https://www.yatra.com/?gclid=Cj0KCQiAiNnuBRD3ARIsAM8KmlsRu24I8vXj3ePIJKWZvdudhskClB7Y1VnPzYIC-hCMcPp1HFI1gEIaAmf0EALw_wcB&s_kwcid=AL!7825!3!213303188858!b!!g!!yatra%20com%20online&cid=mc-ps_lob-yb_cmpid-903831115_ctype-search_sname-google_agrp-_kw-") 
        elif"open wifi speed " in query :
                webbrowser.open("https://fast.com/")
        elif"open trivago" in query:
                webbrowser.open("https://www.trivago.in/en?themeId=280&sem_keyword=trivago&sem_creativeid=264221998694&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=1t1&sem_param1=&sem_param2=&sem_campaignid=259742967&sem_adgroupid=24450848727&sem_targetid=kwd-5593367084&sem_location=20471&cip=9119000005&gclid=Cj0KCQiAiNnuBRD3ARIsAM8Kmlv-XQdrCYEQ23bUfuGR5mF3tGL-pQYk2jWKXAMHfiBDBSTuhx9afiMaAv79EALw_wcB")                
        elif"open 1 mg" in query:
                webbrowser.open("https://www.1mg.com/")
        elif"Open duo web" in query:
                webbrowser.open("https://duo.google.com/?web")
        elif"open agriculture cooperation" in query:
                webbrowser.open("http://agricoop.nic.in/")
        elif"open agriculture ngo" in query:
                webbrowser.open("http://krishiyodha.com/")        
        elif"" in query:
                webbrowser.open("")
               

                

      
                      

                              
   