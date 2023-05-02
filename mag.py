import tkinter as tk
from pyautogui import position
from PIL import Image, ImageTk, ImageGrab

ratio = 1.0
new_image = None 
def main11():
    class Application(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self.pack()
            self.master.title("Screen Magnifier")
            self.state_txt = None
            self.state_label = tk.Label(self, text=None)
            self.state_label.pack()
            self.label_img = tk.Label(self, image=None)
            self.label_img.pack()
            self.width = self.master.winfo_width()
            self.mouse_x, self.mouse_y = position()
            self.height = self.master.winfo_height()
            self.bind('<Configure>', self.on_resize)
            self.bind_all('<Key>', self.key_pressed)
            self.bind_all('<MouseWheel>', self.mouse_wheel)
            self.bind_all('<Button-4>', self.mouse_wheel)
            self.bind_all('<Button-5>', self.mouse_wheel)
            self.forever()

        def update_state(self):
            global ratio
            self.mouse_x, self.mouse_y = position()
            self.state_txt = 'X{} | x: {}, y: {} |  w: {}, h: {}'.format(ratio,
                    self.mouse_x, self.mouse_y, self.width, self.height)
            self.state_label['text'] = self.state_txt

        def on_resize(self, event):
            self.width = self.master.winfo_width()
            self.height = self.master.winfo_height()
            self.update_state()

        def key_pressed(self, event):
            if event.keysym == "Escape":
                root.destroy()

        def mouse_wheel(self, event):
            global ratio
            if event.num == 5 or event.delta == -120:
                ratio -= 0.1
            if event.num == 4 or event.delta == 120:
                ratio += 0.1
            ratio = round(ratio, 2)
            if ratio < 1:
                ratio = 1.0

        def forever(self):
            global new_image, ratio
            self.update_state()
            ss_region = (self.mouse_x, self.mouse_y, self.mouse_x +
                    self.width/ratio, self.mouse_y + self.height/ratio) 
            ss_img = ImageGrab.grab(ss_region)
            resized_image = ss_img.resize((round(self.width*ratio),
                round(self.height*ratio)), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized_image)
            self.label_img['image'] = new_image
            self.master.after(round(ratio*25), self.forever)

    root = tk.Tk()
    root.geometry("400x300")
    app = Application(root)
    app.mainloop()