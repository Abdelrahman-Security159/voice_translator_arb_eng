import speech_recognition as sp
import pyttsx3 as px3
import translate_process as tp
#import nltk
#nltk.download('punkt')

rec = sp.Recognizer()

while True:
    try:
        with sp.Microphone() as mic:
            print("Say Something...")
            
            rec.adjust_for_ambient_noise(mic, duration=1)
            audio = rec.listen(mic)
            
            text = rec.recognize_google(audio)
#"Hello bro how are you today I need your help I want to buy this"
#hello nadia how are you this is your camera 
            text = text.lower()
                        
            print(f"Data => {text}")
            list_words = text.split(' ')
            print(f"List => {list_words}")

            translate = tp.Translate()
            final_result = translate.search(list_words)
            
    except sp.UnknownValueError:
        print("Error With Audio")