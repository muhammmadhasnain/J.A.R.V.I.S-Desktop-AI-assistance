import speech_recognition as st
import win32com.client 
import webbrowser
import os
import google.generativeai as genai
from config import apikey
import random




speaker = win32com.client.Dispatch("SAPI.SpVoice")



chatStr = ""
def Ai(prompt):
    global chatStr 
    
    GOOGLE_API_KEY  = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    genai.configure(api_key=GOOGLE_API_KEY)
    model =  genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    text = response.text

    if not os.path.exists("openai"):
        os.mkdir("openai")

    filename = " ".join(prompt.split("intelligence")[1:]).strip()
    with open(f"openai/{filename}.txt", "w") as f:
        f.write(text)
        



def chat(prompt):
    GOOGLE_API_KEY  = apikey
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model =  genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    say(response.text)
    return response.text




def say(text):
    speaker.Speak(text)


def take_comand():
    r = st.Recognizer()
    with st.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print('Welcome to Jarvis A.I')
    say("hy I am Jarvis Ai")
    while True:
        print("listen ...")
        query = take_comand()
        query = query or ""
        
        say(query)

        sites = [["google", "https://google.com"], ["chat gpt", "https://chatgpt.com"], ["wikipedia", "https://www.wikipedia.com"]]

        for site in sites:
            if f"open {site[0].lower()}" in query.lower():
                say(f"open {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query.lower():
            path = r"C:\Users\latitude\Downloads\4.avi"
            os.startfile(path)
        elif "open file" in query.lower():
            path = r"C:\Users\latitude\Downloads"
            os.startfile(path)
        
        elif "Using artificial intelligence".lower() in query.lower():
            Ai(prompt = query)
            
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        
        elif "jarvis quit".lower() in query.lower():
            break
        
        else:
            print('chating...')
            chat(prompt=query or "hy")
        
               
           
