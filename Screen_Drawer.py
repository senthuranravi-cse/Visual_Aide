from time import sleep
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import NO
from PIL import ImageGrab,ImageTk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2) 
#sasu and Praveen
def main():
    class ToolWin(tk.Tk):

        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'red'
        def __init__(self):
            tk.Toplevel.__init__(self)
            self._offsetx = 0
            self._offsety = 0
            self.wm_attributes('-topmost',1)
            self.penSelect = tk.BooleanVar()
            self.overrideredirect(1)
            self.geometry('200x200')
            self.penModeId = None
            self.bind('<ButtonPress-1>',self.clickTool) 
            self.bind('<B1-Motion>',self.moveTool) 
            self.old_x= None
            self.old_y = None
            self.eraser_on = False
            self.color = self.DEFAULT_COLOR
            self.line_width = 5.0

            draw = tk.Checkbutton(self,text="Pen",command=self.penDraw,variable=self.penSelect)
            draw.pack()
            cancel = tk.Button(self,text="Quit",command=root.destroy)
            cancel.pack()

        def moveTool(self,event):
            self.geometry("200x200+{}+{}".format(self.winfo_pointerx()-self._offsetx,self.winfo_pointery()-self._offsety))

        def clickTool(self,event):
            self._offsetx = event.x
            self._offsety = event.y

        def penDraw(self):
            if self.penSelect.get():
                self.penModeId = root.bind("<B1-Motion>",self.Draw)
                root.bind('<ButtonRelease-1>', self.reset)
            else:
                root.unbind('<B1-Motion>',self.penModeId)

        def Draw(self,event):
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                fullCanvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                width=self.line_width, fill=paint_color,
                                capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y

        def reset(self, event):
            self.old_x, self.old_y = None, None

    def showTool(): 
        toolWin = ToolWin()
        toolWin.mainloop()


    
    sleep(5)
    root = tk.Tk()
    root.state('zoomed')
    root.overrideredirect(1)
    fullCanvas = tk.Canvas(root)
    background = ImageTk.PhotoImage(ImageGrab.grab(all_screens=True)) 
    fullCanvas.create_image(0,0,anchor="nw",image=background)
    fullCanvas.pack(expand="YES",fill="both")
    root.after(100,showTool)
    root.mainloop()