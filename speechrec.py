import speech_recognition as sr
import time
import serial

text=None

ser=serial.Serial("COM4",9600,timeout=2)
ser.flushInput()

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something: ")
        audio=r.listen(source)
        # query=r.recognize_google(audio,language="eng-in")
        # print(query)
        try:
            text=r.recognize_google(audio)
            print("You said: ",text)
        except:
            print("Sorry could not recognize your voice!")
    if(text=="on"):
        ser.write(b'H')
        print("LED turned ON")
        time.sleep(1)
    elif(text=="of"):
        ser.write(b'L')
        print("LED turned OFF")
        time.sleep(1)
    elif(text=="quit"):
        ser.write(b'L')
        print("LED turned OFF")
        time.sleep(1)
        ser.close()
        break
    else:
        print("Invalid Command!!")
        continue
