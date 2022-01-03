import tkinter as tk
import tkinter.font as tkFont
from FIRST_INNINGS import App as f
class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_571=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_571["font"] = ft
        GMessage_571["fg"] = "#333333"
        GMessage_571["justify"] = "center"
        GMessage_571["text"] = "TEAM"
        GMessage_571.place(x=200,y=70,width=173,height=54)

        GButton_743=tk.Button(root)
        GButton_743["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_743["font"] = ft
        GButton_743["fg"] = "#000000"
        GButton_743["justify"] = "center"
        GButton_743["text"] = "BATTING"
        GButton_743.place(x=250,y=160,width=70,height=25)
        GButton_743["command"] = self.GButton_743_command

        GButton_787=tk.Button(root)
        GButton_787["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_787["font"] = ft
        GButton_787["fg"] = "#000000"
        GButton_787["justify"] = "center"
        GButton_787["text"] = "BOWLING"
        GButton_787.place(x=250,y=220,width=70,height=25)
        GButton_787["command"] = self.GButton_787_command

    def GButton_743_command(self):
        root = tk.Tk()
        app = f(root)
        root.mainloop()

    def GButton_787_command(self):
        root = tk.Tk()
        app = f(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
