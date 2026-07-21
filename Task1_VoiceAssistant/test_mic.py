import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Listening... Speak now.")

    recognizer.adjust_for_ambient_noise(source)

    audio = recognizer.listen(source)

print("Recognizing...")

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)

except Exception as e:
    print("Error:", e)