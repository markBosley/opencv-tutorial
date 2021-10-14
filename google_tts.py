from  gtts import gTTS
article="""
Want to learn how to start a garden, but not sure where to begin? In this post I’ll cover the basics of gardening, and provide links to more detailed information so you can garden with confidence and have fun doing it.
"""

print("hello")

transformer = gTTS(text=article,lang="en")
transformer.save('mattsspeech.mp3')

print("Done")