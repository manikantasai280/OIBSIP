import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)

print("Listening...")

with sr.Microphone() as source:
    audio = recognizer.listen(source)
    print("🔍 Recognizing...")
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said: " + recognized_text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")
