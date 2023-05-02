from time import sleep
from tkinter import *
from tkinter import ttk
import numpy as np
import cv2
import pyautogui
from googlesearch import *
import webbrowser
import speech_recognition as sr
import pyttsx3
import os
from tkinter.messagebox import *
from tkinter.filedialog import *
import string
import random
import tkinter as tk
import WhiteBoard as Wb
from tkinter import messagebox 
import Live_caption as Lc

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def main1():
    top = Tk()
    top.title("Presentation Assistant")
    p1 = PhotoImage(file = 'D:\VS code Programs\SPD PROJECT\image.png')  
    top.iconphoto(False, p1)
    def selection():  # kirthi
        top.wm_state('iconic')
        sleep(2)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        N=9
        res = "D:\VS code Programs\Screenshots\Screenshot"+''.join(random.choices(string.ascii_letters, k=N))
        cv2.imwrite(res+".png", image)
        messagebox.showinfo("showinfo", "Screenshot Saved")

    def selection2():  # praveen1
        top.wm_state('iconic')
        sleep(2)
        win=Tk()
        win.geometry("300x300")
        win.title("Search")

        def cal_sum():
            t1=a.get()
            sum=t1
            webbrowser.open("https://google.com/search?q=%s" % sum)
            
        frame3= Frame(win)
        frame3.pack(pady=10)
        Label(win, text="Search in google", font=('Arial 10')).pack()
        frame1= Frame(win)
        frame1.pack(pady=10)
        a=Entry(win, width=35)
        a.pack()
        frame2 = Frame(win)
        frame2.pack(pady=20)
        Button(win, text="Search", command=cal_sum).pack()
        frame1= Frame(win)
        frame1.pack(pady=10)
        Button(win, text="Exit", command=win.destroy).pack()
        win.mainloop()
        win.mainloop()

    def selection3():  # vicky
        resolution = (1920, 1080)
        top.wm_state('iconic')
        sleep(2)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        N=9
        res = "D:\VS code Programs\Recordings\Recordings"+''.join(random.choices(string.digits, k=N))
        filename = res+".avi"
        fps = 60.0
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live", 480, 270)
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.imshow('Live', frame)
            if cv2.waitKey(1) == ord('w'):
                break
        out.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("showinfo", "ScreenRecorder Saved")
    
    def Selection5():  # sasu
        top.wm_state('iconic')
        sleep(2)
        r = sr.Recognizer()
        def Search():
            webbrowser.open("https://google.com/search?q="+MyText)
        def speech(MyText):
            root = Tk()
            root.geometry("500x500")
            root.title("Window")
            T = tk.Text(root, height = 5, width = 52)
            frame3= Frame(root)
            frame3.pack(pady=10)
            l = Label(root, text = "Did you say.....")
            l.config(font =("Courier", 14))
            Fact =MyText
            frame1= Frame(root)
            frame1.pack(pady=10)
            b1 = Button(root, text = "Search",command = Search)
            frame2= Frame(root)
            frame2.pack(pady=10)
            b2 = Button(root, text = "No",command = Selection5)
            frame4= Frame(root)
            frame4.pack(pady=10)
            b3 = Button(root, text = "Exit",command = root.destroy)
            l.pack()
            T.pack()
            b1.pack()
            b2.pack()
            b3.pack()
            T.insert(tk.END, Fact)
            tk.mainloop()
        try:
            with sr.Microphone() as source2:
                k="Speak"
                SpeakText(k)
                r.adjust_for_ambient_noise(source2, duration=5)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                speech(MyText)
                SpeakText(MyText)

        except sr.RequestError as e:
            MyText="Could not request results"
            speech(MyText)

        except sr.UnknownValueError:
            MyText="Speak Loud..........."
            speech(MyText)

    def Selection6():
        top.wm_state('iconic')
        sleep(2)
        Wb.Paint()

    def Selection9():
        top.wm_state('iconic')
        sleep(2)
        messagebox.showinfo("showinfo", "Subtitles will show in terminal.....")
        Lc.main()

    def Selection4():#Praveen2
        top.wm_state('iconic')
        sleep(2)
        win=Tk()
        win.geometry("300x300")
        win.title("Prouniciation")
        def cal_sum():
            t1=a.get()
            sum=t1
            SpeakText(sum)
        frame1= Frame(win)
        frame1.pack(pady=10)
        Label(win, text="Enter Text", font=('Calibri 10')).pack()
        a=Entry(win, width=35)
        a.pack()
        frame1= Frame(win)
        frame1.pack(pady=10)
        Button(win, text="Speech", command=cal_sum).pack()
        frame1= Frame(win)
        frame1.pack(pady=10)
        Button(win, text="Exit", command=win.destroy).pack()
        win.mainloop()
    
    top.geometry("600x600")
    bg = PhotoImage(file="D:\VS code Programs\SPD PROJECT\light1.png")
    label1 = Label(top, image=bg)
    label1.place(x=0, y=0)
    frame1 = Frame(top)
    frame1.pack(pady=90)
    radio = IntVar()
    R1 = Radiobutton(top, text="Screenshot", variable=radio,value=1, command=selection)
    R1.pack(anchor=W)
    R2 = Radiobutton(top, text="Search", variable=radio, value=2, command=selection2)
    R2.pack(anchor=W)
    R3 = Radiobutton(top, text="ScreenRecorder", variable=radio, value=3,  command=selection3)
    R3.pack(anchor=W)
    R4 = Radiobutton(top, text="Pronunciation", variable=radio, value=4,  command=Selection4)
    R4.pack(anchor=W)
    R5 = Radiobutton(top, text="Speech to Search", variable=radio, value=5,  command=Selection5)
    R5.pack(anchor=W)
    R6 = Radiobutton(top, text="Whiteboard", variable=radio, value=6,  command=Selection6)
    R6.pack(anchor=W)
    R9 = Radiobutton(top, text="Live Caption", variable=radio, value=9,command=Selection9)
    R9.pack(anchor=W)
    frame2 = Frame(top)
    frame2.pack(pady=20)
    cancel = tk.Button(text="Quit",command=top.destroy)
    cancel.pack()
    top.mainloop()