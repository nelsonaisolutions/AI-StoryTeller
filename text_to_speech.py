# Convert the story text to speech and save as "story.mp3"
from gTTS import gTTS
tts = gTTS(story_text, lang='en')
tts.save("story.mp3")