import speech_recognition as sr

r = sr.Recognizer()
file1 = sr.AudioFile('harvard.wav')
file2 = sr.AudioFile('jackhammer.wav')

with file1 as source:
    audio = r.record(source)
Query = r.recognize_google(audio)
print(Query)