import tkinter as tk
import tkinter.font as tkFont
from SELECT2 import App as h
import cx_Oracle
conn=cx_Oracle.connect('system/kannan@//localhost:1521/xe')
cur=conn.cursor()
        

class App:
    def __init__(self, root):
        #setting title
        root.title("SPORTS MANAGEMENT SYSTEM")
        root.configure(background='teal')
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_763=tk.Button(root)
        GButton_763["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_763["font"] = ft
        GButton_763["fg"] = "#009688"
        GButton_763["justify"] = "center"
        GButton_763["text"] = "mi"
        GButton_763.place(x=250,y=400,width=70,height=25)
        GButton_763["command"] = self.GButton_763_command

        GButton_929=tk.Button(root)
        GButton_929["bg"] = "#efefef"
        GButton_929["disabledforeground"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_929["font"] = ft
        GButton_929["fg"] = "#fad400"
        GButton_929["justify"] = "center"
        GButton_929["text"] = "csk"
        GButton_929.place(x=250,y=160,width=70,height=25)
        GButton_929["command"] = self.GButton_929_command

        GButton_105=tk.Button(root)
        GButton_105["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_105["font"] = ft
        GButton_105["fg"] = "#cc0000"
        GButton_105["justify"] = "center"
        GButton_105["text"] = "rcb"
        GButton_105.place(x=250,y=200,width=70,height=25)
        GButton_105["command"] = self.GButton_105_command

        GButton_428=tk.Button(root)
        GButton_428["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_428["font"] = ft
        GButton_428["fg"] = "#1960ed"
        GButton_428["justify"] = "center"
        GButton_428["text"] = "rr"
        GButton_428.place(x=250,y=240,width=70,height=25)
        GButton_428["command"] = self.GButton_428_command

        GButton_287=tk.Button(root)
        GButton_287["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_287["font"] = ft
        GButton_287["fg"] = "#c71585"
        GButton_287["justify"] = "center"
        GButton_287["text"] = "kkr"
        GButton_287.place(x=250,y=120,width=70,height=25)
        GButton_287["command"] = self.GButton_287_command

        GButton_470=tk.Button(root)
        GButton_470["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_470["font"] = ft
        GButton_470["fg"] = "#fb9714"
        GButton_470["justify"] = "center"
        GButton_470["text"] = "srh"
        GButton_470.place(x=250,y=320,width=70,height=25)
        GButton_470["command"] = self.GButton_470_command

        GButton_908=tk.Button(root)
        GButton_908["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_908["font"] = ft
        GButton_908["fg"] = "#3119cf"
        GButton_908["justify"] = "center"
        GButton_908["text"] = "dc"
        GButton_908.place(x=250,y=280,width=70,height=25)
        GButton_908["command"] = self.GButton_908_command

        GButton_192=tk.Button(root)
        GButton_192["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_192["font"] = ft
        GButton_192["fg"] = "#c13535"
        GButton_192["justify"] = "center"
        GButton_192["text"] = "pbks"
        GButton_192.place(x=250,y=360,width=70,height=25)
        GButton_192["command"] = self.GButton_192_command

        GMessage_690=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_690["font"] = ft
        GMessage_690["fg"] = "#333333"
        GMessage_690["justify"] = "center"
        GMessage_690["text"] = "SELECT TEAM"
        GMessage_690.place(x=140,y=40,width=296,height=65)

    def GButton_763_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='mi'")
        cur.execute(select)
        app = h(root,cur,14)
        root.mainloop()


    def GButton_929_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='csk'")
        cur.execute(select)
        app = h(root,cur,1)
        root.mainloop()


    def GButton_105_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='rcb'")
        cur.execute(select)
        app = h(root,cur,66)
        root.mainloop()


    def GButton_428_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='rr'")
        cur.execute(select)
        app = h(root,cur,27)
        root.mainloop()


    def GButton_287_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='kkr'")
        cur.execute(select)
        app = h(root,cur,53)
        root.mainloop()


    def GButton_470_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='srh'")
        cur.execute(select)
        app = h(root,cur,92)
        root.mainloop()


    def GButton_908_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='dc'")
        cur.execute(select)
        app = h(root,cur,40)
        root.mainloop()


    def GButton_192_command(self):
        root = tk.Tk()
        select=("select name from players where t_name='pbks'")
        cur.execute(select)
        app = h(root,cur,79)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
