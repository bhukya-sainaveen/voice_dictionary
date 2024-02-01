# main.py
from gtts import gTTS

from src.audio import play_audio
from src.speech import get_user_input
from src.word_operations import get_word_meaning, get_synonyms, get_antonyms

def main():
    # Welcome message
    text = "Hello Welcome! How could I help you?"
    gTTS(text, lang="en").save("hello.mp3")
    play_audio("hello.mp3")
    
    # User input through speech
    user_input = get_user_input()
    if not user_input: return    
    try:
        print("You said:", user_input)
        
        # Word meaning
        meaning = get_word_meaning(user_input)
        if meaning:
            print(meaning)
            gTTS(meaning, lang="en").save("hello.mp3")
            play_audio("hello.mp3")
            
        # Synonyms
        synonyms = get_synonyms(user_input)
        if synonyms:
            text = "Synonyms: " + ", ".join(synonyms)
            print(text)
            gTTS(text, lang="en").save("hello.mp3")
            play_audio("hello.mp3")
        
        # Antonyms
        antonyms = get_antonyms(user_input)
        if antonyms:
            text = "Antonyms: " + ", ".join(antonyms)
            print(text)
            gTTS(text, lang="en").save("hello.mp3")
            play_audio("hello.mp3")

    except Exception as e:
        print("Can't recognize: " + str(e))

if __name__ == "__main__":
    main()
