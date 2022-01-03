import tkinter as tk
import tkinter.font as tkFont
import cx_Oracle
from diplay1 import dis as n
conn=cx_Oracle.connect('system/kannan@//localhost:1521/xe')
cur=conn.cursor()
class App:
    def __init__(self, root,str1,num):
        #setting title
        self.num=num
        root.title("SELECT")
        root.configure(background = 'black')
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        cur1=[]
        for i in str1:
            cur1.append(i)
            
        
        GMessage_97=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_97["font"] = ft
        GMessage_97["fg"] = "#333333"
        GMessage_97["justify"] = "center"
        GMessage_97["text"] = "SELECT PLAYER"
        GMessage_97.place(x=220,y=10,width=156,height=39)

        GButton_571=tk.Button(root)
        GButton_571["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#000000"
        GButton_571["justify"] = "center"
        GButton_571["text"] = cur1[0]
        GButton_571.place(x=260,y=190,width=70,height=25)
        GButton_571["command"] = self.GButton_571_command

        GButton_406=tk.Button(root)
        GButton_406["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_406["font"] = ft
        GButton_406["fg"] = "#000000"
        GButton_406["justify"] = "center"
        GButton_406["text"] = cur1[1]
        GButton_406.place(x=20,y=70,width=70,height=25)
        GButton_406["command"] = self.GButton_406_command

        GButton_763=tk.Button(root)
        GButton_763["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_763["font"] = ft
        GButton_763["fg"] = "#000000"
        GButton_763["justify"] = "center"
        GButton_763["text"] = cur1[2]
        GButton_763.place(x=20,y=190,width=70,height=25)
        GButton_763["command"] = self.GButton_763_command

        GButton_166=tk.Button(root)
        GButton_166["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_166["font"] = ft
        GButton_166["fg"] = "#000000"
        GButton_166["justify"] = "center"
        GButton_166["text"] = cur1[3]
        GButton_166.place(x=20,y=130,width=70,height=25)
        GButton_166["command"] = self.GButton_166_command

        GButton_104=tk.Button(root)
        GButton_104["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_104["font"] = ft
        GButton_104["fg"] = "#000000"
        GButton_104["justify"] = "center"
        GButton_104["text"] = cur1[4]
        GButton_104.place(x=500,y=70,width=70,height=25)
        GButton_104["command"] = self.GButton_104_command

        GButton_636=tk.Button(root)
        GButton_636["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_636["font"] = ft
        GButton_636["fg"] = "#000000"
        GButton_636["justify"] = "center"
        GButton_636["text"] = cur1[5]
        GButton_636.place(x=20,y=250,width=70,height=25)
        GButton_636["command"] = self.GButton_636_command

        GButton_984=tk.Button(root)
        GButton_984["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_984["font"] = ft
        GButton_984["fg"] = "#000000"
        GButton_984["justify"] = "center"
        GButton_984["text"] = cur1[6]
        GButton_984.place(x=500,y=190,width=70,height=25)
        GButton_984["command"] = self.GButton_984_command

        GButton_747=tk.Button(root)
        GButton_747["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_747["font"] = ft
        GButton_747["fg"] = "#000000"
        GButton_747["justify"] = "center"
        GButton_747["text"] = cur1[7]
        GButton_747.place(x=260,y=250,width=70,height=25)
        GButton_747["command"] = self.GButton_747_command

        GButton_86=tk.Button(root)
        GButton_86["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_86["font"] = ft
        GButton_86["fg"] = "#000000"
        GButton_86["justify"] = "center"
        GButton_86["text"] = cur1[8]
        GButton_86.place(x=500,y=130,width=70,height=25)
        GButton_86["command"] = self.GButton_86_command

        GButton_496=tk.Button(root)
        GButton_496["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_496["font"] = ft
        GButton_496["fg"] = "#000000"
        GButton_496["justify"] = "center"
        GButton_496["text"] = cur1[9]
        GButton_496.place(x=260,y=70,width=70,height=25)
        GButton_496["command"] = self.GButton_496_command

        GButton_686=tk.Button(root)
        GButton_686["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_686["font"] = ft
        GButton_686["fg"] = "#000000"
        GButton_686["justify"] = "center"
        GButton_686["text"] = cur1[10]
        GButton_686.place(x=500,y=250,width=70,height=25)
        GButton_686["command"] = self.GButton_686_command

        GButton_623=tk.Button(root)
        GButton_623["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_623["font"] = ft
        GButton_623["fg"] = "#000000"
        GButton_623["justify"] = "center"
        GButton_623["text"] = cur1[11]
        GButton_623.place(x=20,y=310,width=70,height=25)
        GButton_623["command"] = self.GButton_623_command

        GButton_693=tk.Button(root)
        GButton_693["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_693["font"] = ft
        GButton_693["fg"] = "#000000"
        GButton_693["justify"] = "center"
        GButton_693["text"] = cur1[12]
        GButton_693.place(x=500,y=310,width=70,height=25)
        GButton_693["command"] = self.GButton_693_command

        GButton_24=tk.Button(root)
        GButton_24["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_24["font"] = ft
        GButton_24["fg"] = "#000000"
        GButton_24["justify"] = "center"
        GButton_24["text"] = "Button"
        GButton_24.place(x=260,y=130,width=70,height=25)
        GButton_24["command"] = self.GButton_24_command

        GButton_257=tk.Button(root)
        GButton_257["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_257["font"] = ft
        GButton_257["fg"] = "#000000"
        GButton_257["justify"] = "center"
        GButton_257["text"] = "Button"
        GButton_257.place(x=260,y=310,width=70,height=25)
        GButton_257["command"] = self.GButton_257_command

    def GButton_571_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num)
        root.mainloop()


    def GButton_406_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+1)
        root.mainloop()


    def GButton_763_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+2)
        root.mainloop()


    def GButton_166_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+3)
        root.mainloop()


    def GButton_104_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+4)
        root.mainloop()


    def GButton_636_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+5)
        root.mainloop()


    def GButton_984_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+6)
        root.mainloop()

    def GButton_747_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+7)
        root.mainloop()


    def GButton_86_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+8)
        root.mainloop()


    def GButton_496_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+9)
        root.mainloop()


    def GButton_686_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+10)
        root.mainloop()


    def GButton_623_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+11)
        root.mainloop()


    def GButton_693_command(self):
        root=tk.Tk()
        cur.execute('select * from players')
        m=n(root,cur,self.num+12)
        root.mainloop()


    def GButton_24_command(self):
        print("command")


    def GButton_257_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root,cur,num)
    root.mainloop()
