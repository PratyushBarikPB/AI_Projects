import speech_recognition as sr
import os
import time
from gtts import gTTS
import win32com.client
import webbrowser
import openai
import datetime
import random
from config import apikey

# import contoller as cnt

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatpb = ""


def chat(cmd):
    global chatpb
    openai.api_key = apikey
    chatpb += f"Pratyush: {cmd}\n JARVIS: "
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": chatpb
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this insisde a try catch block
    speak(response.choices[0].message.content)
    chatpb += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content
    # if not os.path.exists(("Openaipb")):
    #     os.mkdir("Openaipb")

    # with open(f"Openaipb/prompt- {random.randint(1,324324324)}","w") as f:
    with open(f"Openaipb/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ******************\n\n"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this insisde a try catch block
    print(response.choices[0].message.content)
    text += response.choices[0].message.content
    if not os.path.exists(("Openaipb")):
        os.mkdir("Openaipb")

    # with open(f"Openaipb/prompt- {random.randint(1,324324324)}","w") as f:
    with open(f"Openaipb/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def speak(text):
    # tts=gTTS(text=text, lang="en-in")
    filename = text
    # tts.save(filename)
    speaker.Speak(filename)


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=1
        audio = r.listen(source)
        said = ""
        try:
            print("Identifying...")
            said = r.recognize_google(audio, language="en-in")
            print(f"User said: {said}")
        except Exception as e:
            speak("Some Exception occur. Sorry from JARVIS")
    return said


speak("HELLO I am JARVIS How can I help you")
while True:
    print("Listning...")
    cmd = command()
    # todo: Add more websites
    sites = [["youtube", "www.youtube.com"], ["wikipedia", "www.wikipedia.com"], ["google", "www.google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in cmd.lower():
            speak(f"Opening {site[0]} Sir...")
            webbrowser.open(site[1])

    if "the time".lower() in cmd.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strfTime}")

    elif "open camera".lower() in cmd.lower():
        os.system(f"start microsoft.windows.camera:")

    elif "open calculator".lower() in cmd.lower():
        os.system(f"start calc")

    elif "Artificial Intelligence".lower() in cmd.lower():
        ai(prompt=cmd)
    elif "Jarvis quit".lower() in cmd.lower():
        speak("ok sir...")
        exit()
    elif "reset chat".lower() in cmd.lower():
        chatpb = ""
    elif "light on".lower() in cmd.lower():
        speak("Turning on the light...")
        cnt.led(1)
    elif "light off".lower() in cmd.lower():
        speak("Turning off the light...")
        cnt.led(0)
    else:
        print("I am there for you...")
        chat(cmd)

# if "hello" in text:
#     speak("How are you doing")


# speaker=win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     print("Enter the word you want to speak if out by computer")
#     # s=input()
#     speaker.Speak("HI")