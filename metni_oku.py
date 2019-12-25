from gtts import gTTS 
import os

tts = gTTS(text="Merhaba Dünya",lang="tr")
tts.save("ses.mp3")

os.system("ses.mp3")