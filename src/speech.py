# speech.py
import speech_recognition as sr

def get_user_input():
    r = sr.Recognizer()
    r.energy_threshold = 5000

    with sr.Microphone() as source:
        print("Speak any word for meaning:")
        try:
            audio = r.listen(source, timeout=10) 
            return r.recognize_google(audio, show_all=False)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error during speech recognition: {e}")
