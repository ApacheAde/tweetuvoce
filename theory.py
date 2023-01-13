from gtts import gTTS

# Text to be converted to speech
text = input("Enter Text: ")



# Create gTTS object
tts = gTTS(text=text)

# Save the audio file
tts.save("audio.mp3")
