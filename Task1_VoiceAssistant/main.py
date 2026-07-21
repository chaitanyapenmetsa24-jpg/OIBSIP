import os
import webbrowser
import wikipedia
import datetime
import asyncio
import edge_tts

VOICE = "en-US-GuyNeural"


def speak(text):
    print(text)

    async def _speak():
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save("voice.mp3")

    asyncio.run(_speak())

    os.system('start "" voice.mp3')


def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning, Chaitanya! I am your Voice Assistant.")
    elif hour < 18:
        speak("Good Afternoon, Chaitanya! I am your Voice Assistant.")
    else:
        speak("Good Evening, Chaitanya! I am your Voice Assistant.")


wish()

while True:

    command = input("\nEnter your command: ").lower()

    if command == "":

        continue

    elif "hello" in command:

        speak("Hello Chaitanya! How can I help you?")

    elif "time" in command:

        current = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {current}")

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}")

    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:

        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open chatgpt" in command:

        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif command.startswith("search "):

        query = command.replace("search ", "")

        speak(f"Searching Wikipedia for {query}")

        try:
            wikipedia.set_lang("en")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        except wikipedia.exceptions.DisambiguationError:
            speak("Your search has multiple results. Please be more specific.")

        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find that topic.")

        except Exception:
            speak("Unable to search Wikipedia.")

    elif "exit" in command or "quit" in command:

        speak("Goodbye Chaitanya. Have a nice day.")
        break

    else:

        speak("Sorry, I don't understand.")