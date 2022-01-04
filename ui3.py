import tkinter as tk
import tkinter.font as tkFont
from update1 import App as a
from SELECT1 import App as g
from POINTSTABLE import table as z
import cx_Oracle
class App:
    def __init__(self, root):
        #setting title
        root.title("SPORTS MANAGEMENT SYSTEM")
        root.configure(background='blue')
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_512=tk.Button(root)
        GButton_512["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_512["font"] = ft
        GButton_512["fg"] = "#000000"
        GButton_512["justify"] = "center"
        GButton_512["text"] = "UPDATE MATCH INFORMATION"
        GButton_512.place(x=160,y=100,width=237,height=36)
        GButton_512["command"] = self.GButton_512_command

        GButton_785=tk.Button(root,text='select team')
        GButton_785["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_785["font"] = ft
        GButton_785["justify"] = "center"
        GButton_785["text"] = "SELECT TEAM TO VIEW STATS"
        GButton_785.place(x=160,y=150,width=237,height=36)
        GButton_785["command"] = self.GButton_785_command

        GButton_806=tk.Button(root)
        GButton_806["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_806["font"] = ft
        GButton_806["fg"] = "#000000"
        GButton_806["justify"] = "center"
        GButton_806["text"] = "POINTS TABLE"
        GButton_806.place(x=230,y=200,width=110,height=38)
        GButton_806["command"] = self.GButton_806_command

        GMessage_38=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_38["font"] = ft
        GMessage_38["fg"] = "#333333"
        GMessage_38["justify"] = "center"
        GMessage_38["text"] = "INDIAN PREMIER LEAGUE"
        GMessage_38["relief"] = "groove"
        GMessage_38.place(x=100,y=10,width=366,height=66)

    def GButton_512_command(self):        
        root1 = tk.Tk()
        app1 = a(root1)
        root1.mainloop()

    def GButton_785_command(self):
        root = tk.Tk()
        app = g(root)
        root.mainloop()

    def GButton_806_command(self):
        root = tk.Tk()
        app = z(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
