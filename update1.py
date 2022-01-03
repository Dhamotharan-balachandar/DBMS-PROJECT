import cx_Oracle
import tkinter as tk
import tkinter.font as tkFont
from TEAM1_SELECTION import App as e
import tkinter as tk
import tkinter.font as tkFont
conn=cx_Oracle.connect('system/kannan@//localhost:1521/xe')
cur=conn.cursor()

class App:
    def __init__(self, root):
        self.v=[]
        self.call663 = 0
        self.call534 = 0
        self.call119 = 0
        self.call827 = 0
        self.call924 = 0
        self.call494 = 0
        self.call622 = 0
        self.call436 = 0
        self.players = 0
        #setting title
        root.title("undefined")
        root.configure(background = "teal")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_521=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_521["font"] = ft
        GMessage_521["fg"] = "#333333"
        GMessage_521["justify"] = "center"
        GMessage_521["text"] = "SELECT 2 TEAMS FOR MATCHUP"
        GMessage_521.place(x=200,y=0,width=205,height=79)

        GCheckBox_663=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_663["font"] = ft
        GCheckBox_663["fg"] = "#333333"
        GCheckBox_663["justify"] = "center"
        GCheckBox_663["text"] = "CSK"
        GCheckBox_663.place(x=260,y=110,width=70,height=25)
        GCheckBox_663["offvalue"] = "1"
        GCheckBox_663["onvalue"] = "1"
        GCheckBox_663["command"] = self.GCheckBox_663_command

        GCheckBox_534=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_534["font"] = ft
        GCheckBox_534["fg"] = "#333333"
        GCheckBox_534["justify"] = "center"
        GCheckBox_534["text"] = "RCB"
        GCheckBox_534.place(x=260,y=150,width=70,height=25)
        GCheckBox_534["offvalue"] = "1"
        GCheckBox_534["onvalue"] = "1"
        GCheckBox_534["command"] = self.GCheckBox_534_command

        GCheckBox_119=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_119["font"] = ft
        GCheckBox_119["fg"] = "#333333"
        GCheckBox_119["justify"] = "center"
        GCheckBox_119["text"] = "DC"
        GCheckBox_119.place(x=260,y=190,width=70,height=25)
        GCheckBox_119["offvalue"] = "1"
        GCheckBox_119["onvalue"] = "1"
        GCheckBox_119["command"] = self.GCheckBox_119_command

        GCheckBox_827=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_827["font"] = ft
        GCheckBox_827["fg"] = "#333333"
        GCheckBox_827["justify"] = "center"
        GCheckBox_827["text"] = "MI"
        GCheckBox_827.place(x=260,y=230,width=70,height=25)
        GCheckBox_827["offvalue"] = "1"
        GCheckBox_827["onvalue"] = "1"
        GCheckBox_827["command"] = self.GCheckBox_827_command

        GCheckBox_924=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_924["font"] = ft
        GCheckBox_924["fg"] = "#333333"
        GCheckBox_924["justify"] = "center"
        GCheckBox_924["text"] = "PBKS"
        GCheckBox_924.place(x=260,y=270,width=70,height=25)
        GCheckBox_924["offvalue"] = "1"
        GCheckBox_924["onvalue"] = "1"
        GCheckBox_924["command"] = self.GCheckBox_924_command

        GCheckBox_494=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_494["font"] = ft
        GCheckBox_494["fg"] = "#333333"
        GCheckBox_494["justify"] = "center"
        GCheckBox_494["text"] = "KKR"
        GCheckBox_494.place(x=260,y=310,width=70,height=25)
        GCheckBox_494["offvalue"] = "1"
        GCheckBox_494["onvalue"] = "1"
        GCheckBox_494["command"] = self.GCheckBox_494_command

        GCheckBox_622=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_622["font"] = ft
        GCheckBox_622["fg"] = "#333333"
        GCheckBox_622["justify"] = "center"
        GCheckBox_622["text"] = "RR"
        GCheckBox_622.place(x=260,y=350,width=70,height=25)
        GCheckBox_622["offvalue"] = "1"
        GCheckBox_622["onvalue"] = "1"
        GCheckBox_622["command"] = self.GCheckBox_622_command

        GCheckBox_436=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_436["font"] = ft
        GCheckBox_436["fg"] = "#333333"
        GCheckBox_436["justify"] = "center"
        GCheckBox_436["text"] = "SRH"
        GCheckBox_436.place(x=260,y=390,width=70,height=25)
        GCheckBox_436["offvalue"] = "1"
        GCheckBox_436["onvalue"] = "1"
        GCheckBox_436["command"] = self.GCheckBox_436_command

    def GCheckBox_663_command(self):
        if(self.call663 == 0):
            cur.execute("select p_id,name from players where t_name='csk'")
            self.call663 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass

    def GCheckBox_534_command(self):
        if(self.call534 == 0):
            cur.execute("select p_id,name from players where t_name='rcb'")
            self.call534 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_119_command(self):
        if(self.call119 == 0):
            cur.execute("select p_id,name from players where t_name='dc'")
            self.call119 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_827_command(self):
        if(self.call827 == 0):
            cur.execute("select p_id,name from players where t_name='mi'")
            self.call827 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass

    def GCheckBox_924_command(self):
        if(self.call924 == 0):
            cur.execute("select p_id,name from players where t_name='pbks'")
            self.call924 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_494_command(self):
        if(self.call494 == 0):
            cur.execute("select p_id,name from players where t_name='kkr'")
            self.call494 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass

    def GCheckBox_622_command(self):
        if(self.call622 == 0):
            cur.execute("select p_id,name from players where t_name='rr'")
            self.call622 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass

    def GCheckBox_436_command(self):
        if(self.call436 == 0):
            cur.execute("select p_id,name from players where t_name='srh'")
            self.call436 += 1
            self.players += 1
            for i in cur:
                self.v.append(i)
        if(self.players == 2):
            root = tk.Tk()
            app = e(root,self.v)
            root.mainloop()
        else:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

