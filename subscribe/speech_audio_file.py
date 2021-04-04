import gtts
from playsound import playsound

def text_to_audio_file():
	tts = gtts.gTTS(input("Enter text that can be converted into audio file:\n"))
	file_name = input("Enter a file name:\n")
	tts.save(file_name+".mp3")
	playsound(file_name+".mp3")

