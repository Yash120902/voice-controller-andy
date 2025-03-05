# -*- coding: utf-8 -*-
from tkinter import *
import ctypes
import speech_recognition as sr
import pyttsx3
import os
import subprocess
import wikipedia
import winshell
import webbrowser
from ecapture import ecapture as ec
#****************pyttsx**********
speakerRate = {"snail": 200 - 199, "slow": 200 - 130, "normal": 200 - 65, "fast": 200 + 60}  # 200 is default
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', speakerRate["normal"])
engine.setProperty('voice', voices[1].id)
root=Tk()
root.resizable(False,False)
w=300
h=500
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
x=(sw/2) - (w/2)
y = (sh/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Andy Here!")
#*****************images*************
back=PhotoImage(file="images/Background.png")
listen_image=PhotoImage(file="images/listening.gif")
idle_image=PhotoImage(file="images/idle1.gif")
frame1=Frame(root,width=300,height=430)
frame1.pack()
frame2=Frame(root,width=300,height=70)
frame2.pack()
frame1.pack_propagate(0)
back_label=Label(frame1,width=300,height=430,image=back)
back_label.place(x=0, y=0, relwidth=1, relheight=1)
status=Label(frame1,text="Idle",bg="Red")
status.pack(side=TOP)
#******* image capture function*************
def img():
    
    import pygame
    import pygame.camera
 
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()

    if camlist:
        cam = pygame.camera.Camera(camlist[0], (640, 480))
        cam.start()
        image = cam.get_image()
        pygame.image.save(image, "filename.jpg")
    else:
        print("No camera on current device")

#*********pyttsx3 function*******
def real_work():
    button_one.configure(image=listen_image)
    button_one.update_idletasks()


    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        ("Say something!")
        status.configure(text="Active",bg="Green")
        status.update()
        audio = r.listen(source, timeout=20, phrase_time_limit=20)
        print("listened")
        status.configure(text="Idle",bg="Red")
        status.update()

        button_one.configure(image=idle_image)
        button_one.update()

    try:
        cmd = r.recognize_google(audio)
        print(cmd)
        cmd=cmd.split()[-1]
        print(cmd)
        cmd=str(cmd)
        cmd=cmd.lower()
        question = Label(frame1, font=12, text="Me:"+cmd, anchor="w")
        question.pack(side=TOP, fill=X)
        frame1.update()


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    #******* conditions to call commands *******

    if (cmd in "lock my device") :
          answer=Label(frame1, font=12, text="Andy:Locking Screen", anchor="w")
          answer.pack(side=TOP, fill=X)
          frame1.update()
          engine.say("locking screen")
          engine.runAndWait()
          frame1.update()
          ctypes.windll.user32.LockWorkStation()
          answer.destroy()
          question.destroy()
    elif(cmd in "hello martin"):
        answer = Label(frame1, font=12, text="Andy: Hello Yash, How are you ?", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        answer.destroy()
        engine.say("Hello Yash, How are you ?")
        engine.runAndWait()
        answer.destroy()
    elif(cmd in "you"):
        answer = Label(frame1, font=12, text="Andy: I am Totaly fine Yash! ", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("I am Totaly fine Yash, Thank you")
        engine.runAndWait()
        frame1.update()
        answer.destroy()
        
    elif(cmd in "shutdown"):
        answer = Label(frame1, font=12, text="Andy:Shutting Down Your System", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Shutting Down Your System")
        engine.runAndWait()
        frame1.update()
        os.system("shutdown /s /t 1")
        answer.destroy()
    elif(cmd in"exit"):
            engine.say("Bye Bye")
            engine.runAndWait()
            root.quit()
    elif(cmd in"browser"):
        answer = Label(frame1, font=12, text="Andy:Opening web browser", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Openng web browser")
        engine.runAndWait()
        frame1.update()
        #subprocess.call("C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        os.startfile(r'"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"')
        #subprocess.call("C:\Program Files\Internet Explorer\iexplore.exe")
        answer.destroy()
        #os.startfile(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    elif (cmd == "player"):
        answer = Label(frame1, font=12, text="Andy:Opening vlc", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("opening vlc")
        engine.runAndWait()
        frame1.update()
        os.startfile(r'"C:\Program Files\VideoLAN\VLC\vlc.exe"')
        #subprocess.call("C:\Program Files\VideoLAN\VLC\vlc.exe")
        answer.destroy()
    elif "camera" in cmd or "take a photo" in cmd:
            ec.capture(0, "frame", "img.jpg")
    elif (cmd == "computer"):
        answer = Label(frame1, font=12, text="Andy:Opening my computer", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("opening my computer")
        engine.runAndWait()
        frame1.update()
        os.startfile(r'"C:\\Windows\\explorer.exe"')
        answer.destroy()
    elif (cmd in "calculator"):
        answer = Label(frame1, font=12, text="Andy:Opening calculator", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening calculator")
        engine.runAndWait()
        frame1.update()
        os.system('C:\Windows\System32\calc.exe')
        answer.destroy()
        #os.startfile("C:/Windows/System32/calc.exe")
        #os.startfile("C:/Windows/System32/calc.exe")
    elif (cmd in "control panel"):
        answer = Label(frame1, font=12, text="Andy:Opening control panel", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening control panel")
        engine.runAndWait()
        frame1.update()
        subprocess.call("C:\Windows\System32\control.exe")
        answer.destroy()
        #os.startfile(r'"C:\Windows\System32\control.exe"')
    elif(cmd in "wikipedia"):
        answer = Label(frame1, font=12, text="Andy:what you want to search about", anchor="w")
        answer.pack(side=TOP,fill=X)
        frame1.update()
        engine.say("what you want to search about")
        engine.runAndWait()
        status.configure(text="Active",bg="Green")
        answer.destroy()
        status.update()
        answer.destroy()
        button_one.configure(image=listen_image)
        button_one.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
         audio = r.listen(source)
         status.configure(text="Idle",bg="Red")
         status.update()
         button_one.configure(image=idle_image)
         button_one.update()
         frame1.update()
        cmd = r.recognize_google(audio)
        print(cmd)
        answer = Label(frame1, font=12, text="Me:"+cmd, anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        result = wikipedia.summary(cmd, sentences=2)
        answer.destroy()
        frame1.update()
        answer = Label(frame1, font=12, text="Andy:"+result,justify="left",wraplength=275, anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say(result)
        engine.runAndWait()
        answer.destroy()
        question.destroy()
        frame1.update()
    elif(cmd in "recyclebin"):
        answer = Label(frame1, font=12, text="Andy:recycle bin cleared", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("recycle bin cleared")
        engine.runAndWait()
        frame1.update()
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        answer.destroy()
    elif (cmd in "music"):
        answer = Label(frame1, font=12, text="Andy:playing music", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("playing music")
        engine.runAndWait()
        os.startfile("C:/Users/yhkki/Desktop/songs/apocalypse.mp3")
        frame1.update()
        answer.destroy()
    elif (cmd == "video"):
        answer = Label(frame1, font=12, text="Andy:playing video", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("playing video")
        engine.runAndWait()
        os.startfile("C:/Users/yhkki/Downloads/Video/djsnake.mp4")
        frame1.update()
        answer.destroy()
    elif (cmd in "images"):
        answer = Label(frame1, font=12, text="Andy:opening image", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("opening image")
        engine.runAndWait()
        os.system('start C:/Users/yhkki/Desktop/plusxlogo.png')
        frame1.update()
        answer.destroy()
    elif (cmd in "settings"):
        answer = Label(frame1, font=12, text="Andy:Opening settings", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("opening settings")
        engine.runAndWait()
        os.system('start ms-settings:')
        frame1.update()
        answer.destroy()
    elif (cmd in "bluetooth"):
        answer = Label(frame1, font=12, text="Andy:opening bluetooth settings", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("opening bluetooth settings")
        engine.runAndWait()
        os.system('control.exe bthprops.cpl')
        frame1.update()
        answer.destroy()
    elif (cmd in "uninstall programs"):
        answer = Label(frame1, font=12, text="Andy:Opening programs settings", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening programs settings")
        engine.runAndWait()
        os.system('control.exe appwiz.cpl')
        frame1.update()
        answer.destroy()
    elif(cmd in "photo"):
        answer = Label(frame1, font=12, text="Andy:Capturing image !", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        answer.destroy()
        engine.say("Capturing image !")
        engine.runAndWait()
        os.system ('img()')
        answer.destroy()
    elif (cmd in "scanner"):
        answer = Label(frame1, font=12, text="Andy:Opening scanner settings", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening scanner settings")
        engine.runAndWait()
        os.system('control.exe sticpl.cpl')
        frame1.update()
        answer.destroy()
    elif (cmd in "properties"):
        answer = Label(frame1, font=12, text="Andy:Opening system properties", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening system properties")
        engine.runAndWait()
        os.system('control.exe sysdm.cpl')
        frame1.update()
        answer.destroy()
    elif (cmd in "open Windows firewall"):
        answer = Label(frame1, font=12, text="Andy:Opening Windows firewall", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Opening Windows firewall")
        engine.runAndWait()
        os.system('control.exe firewall.cpl')
        frame1.update()
        answer.destroy()
   
    elif (cmd in "signout"):
        answer = Label(frame1, font=12, text="Andy:logging out", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("logging out")
        engine.runAndWait()
        os.system("shutdown -l")
        frame1.update()
        answer.destroy()
    elif (cmd in "sleep"):
        answer = Label(frame1, font=12, text="Andy:going to sleep", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("going to sleep")
        engine.runAndWait()
        os.system("shutdown.exe /h")
        frame1.update()
        answer.destroy()
    elif (cmd in "google"):
        answer = Label(frame1, font=12, text="Andy:searching in google", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Searching in google")
        engine.runAndWait()
        url = "https://www.kuk.ac.in"
        webbrowser.open(url)
        frame1.update()
        answer.destroy()
    elif (cmd in "google"):
        answer = Label(frame1, font=12, text="Andy:what you want to search about", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("what you want to search about")
        engine.runAndWait()
        status.configure(text="Active", bg="Green")
        answer.destroy()
        status.update()
        button_one.configure(image=listen_image)
        button_one.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            status.configure(text="Idle", bg="Red")
            status.update()
            button_one.configure(image=idle_image)
            button_one.update()
            frame1.update()
        cmd = r.recognize_google(audio)
        print(cmd)
        answer = Label(frame1, font=12, text="Me:" + cmd, anchor="w")
        answer.pack(side=TOP, fill=X)
        engine.say(cmd)
        engine.runAndWait()
        engine.say("Searching in google")
        engine.runAndWait()
        url = "https://www.google.com.tr/search?q={}".format(cmd)
        webbrowser.open(url)
        frame1.update()
        answer.destroy()
        question.destroy()
        frame1.update()
    elif (cmd in "signout"):
        answer = Label(frame1, font=12, text="Andy:logging out", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("logging out")
        engine.runAndWait()
        os.system("shutdown -l")
        frame1.update()
        answer.destroy()
    else:
        answer = Label(frame1, font=12, text="Andy:Command not found", anchor="w")
        answer.pack(side=TOP, fill=X)
        frame1.update()
        engine.say("Command not found")
        engine.runAndWait()
        answer.destroy()
        frame1.update()

    question.destroy()

button_one=Button(frame2,image=idle_image,border=1,command=real_work)
button_one.pack(side=BOTTOM)
mainloop()
