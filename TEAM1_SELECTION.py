import tkinter as tk
import tkinter.font as tkFont
from TEAM2_SELECTION import App as d
class App:
    def __init__(self,root,v):
        self.v=v
        self.b=[]
        self.call265 = 0
        self.call861 = 0
        self.call653 = 0
        self.call308 = 0
        self.call194 = 0
        self.call986 = 0
        self.call680 = 0
        self.call811 = 0
        self.call845 = 0
        self.call271 = 0
        self.call794 = 0
        self.call791 = 0
        self.call41 = 0
        self.call653 = 0
        self.call962 = 0
        self.call117 = 0
        self.players = 0
        #setting title
        root.title("SPORTS MANAGEMENT SYSTEM")
        root.configure(background = "brown")
        #setting window size
        width=686
        height=587
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GCheckBox_265=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_265["font"] = ft
        GCheckBox_265["fg"] = "#333333"
        GCheckBox_265["justify"] = "center"
        GCheckBox_265["text"] = self.v[0]
        GCheckBox_265.place(x=10,y=150,width=150,height=50)
        GCheckBox_265["offvalue"] = "1"
        GCheckBox_265["onvalue"] = "1"
        GCheckBox_265["command"] = self.GCheckBox_265_command

        GLabel_943=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_943["font"] = ft
        GLabel_943["fg"] = "#333333"
        GLabel_943["justify"] = "center"
        GLabel_943["text"] = "SELECT 11 PLAYERS"
        GLabel_943.place(x=260,y=0,width=126,height=56)

        GCheckBox_861=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_861["font"] = ft
        GCheckBox_861["fg"] = "#333333"
        GCheckBox_861["justify"] = "center"
        GCheckBox_861["text"] = self.v[1]
        GCheckBox_861.place(x=10,y=310,width=150,height=50)
        GCheckBox_861["offvalue"] = "1"
        GCheckBox_861["onvalue"] = "1"
        GCheckBox_861["command"] = self.GCheckBox_861_command

        GCheckBox_653=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_653["font"] = ft
        GCheckBox_653["fg"] = "#333333"
        GCheckBox_653["justify"] = "center"
        GCheckBox_653["text"] = self.v[2]
        GCheckBox_653.place(x=460,y=310,width=150,height=50)
        GCheckBox_653["offvalue"] = "1"
        GCheckBox_653["onvalue"] = "1"
        GCheckBox_653["command"] = self.GCheckBox_653_command

        GCheckBox_308=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_308["font"] = ft
        GCheckBox_308["fg"] = "#333333"
        GCheckBox_308["justify"] = "center"
        GCheckBox_308["text"] = self.v[3]
        GCheckBox_308.place(x=250,y=390,width=150,height=50)
        GCheckBox_308["offvalue"] = "1"
        GCheckBox_308["onvalue"] = "1"
        GCheckBox_308["command"] = self.GCheckBox_308_command

        GCheckBox_194=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_194["font"] = ft
        GCheckBox_194["fg"] = "#333333"
        GCheckBox_194["justify"] = "center"
        GCheckBox_194["text"] = self.v[4]
        GCheckBox_194.place(x=250,y=150,width=150,height=50)
        GCheckBox_194["offvalue"] = "1"
        GCheckBox_194["onvalue"] = "1"
        GCheckBox_194["command"] = self.GCheckBox_194_command

        GCheckBox_986=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_986["font"] = ft
        GCheckBox_986["fg"] = "#333333"
        GCheckBox_986["justify"] = "center"
        GCheckBox_986["text"] = self.v[5]
        GCheckBox_986.place(x=10,y=230,width=150,height=50)
        GCheckBox_986["offvalue"] = "1"
        GCheckBox_986["onvalue"] = "1"
        GCheckBox_986["command"] = self.GCheckBox_986_command

        GCheckBox_680=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_680["font"] = ft
        GCheckBox_680["fg"] = "#333333"
        GCheckBox_680["justify"] = "center"
        GCheckBox_680["text"] = self.v[6]
        GCheckBox_680.place(x=460,y=70,width=150,height=50)
        GCheckBox_680["offvalue"] = "1"
        GCheckBox_680["onvalue"] = "1"
        GCheckBox_680["command"] = self.GCheckBox_680_command

        GCheckBox_811=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_811["font"] = ft
        GCheckBox_811["fg"] = "#333333"
        GCheckBox_811["justify"] = "center"
        GCheckBox_811["text"] = self.v[7]
        GCheckBox_811.place(x=250,y=310,width=150,height=50)
        GCheckBox_811["offvalue"] = "1"
        GCheckBox_811["onvalue"] = "1"
        GCheckBox_811["command"] = self.GCheckBox_811_command

        GCheckBox_845=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_845["font"] = ft
        GCheckBox_845["fg"] = "#333333"
        GCheckBox_845["justify"] = "center"
        GCheckBox_845["text"] = self.v[8]
        GCheckBox_845.place(x=250,y=230,width=150,height=50)
        GCheckBox_845["offvalue"] = "1"
        GCheckBox_845["onvalue"] = "1"
        GCheckBox_845["command"] = self.GCheckBox_845_command

        GCheckBox_271=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_271["font"] = ft
        GCheckBox_271["fg"] = "#333333"
        GCheckBox_271["justify"] = "center"
        GCheckBox_271["text"] = self.v[9]
        GCheckBox_271.place(x=10,y=70,width=150,height=50)
        GCheckBox_271["offvalue"] = "1"
        GCheckBox_271["onvalue"] = "1"
        GCheckBox_271["command"] = self.GCheckBox_271_command

        GCheckBox_794=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_794["font"] = ft
        GCheckBox_794["fg"] = "#333333"
        GCheckBox_794["justify"] = "center"
        GCheckBox_794["text"] = self.v[10]
        GCheckBox_794.place(x=250,y=70,width=150,height=50)
        GCheckBox_794["offvalue"] = "1"
        GCheckBox_794["onvalue"] = "1"
        GCheckBox_794["command"] = self.GCheckBox_794_command

        GCheckBox_791=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_791["font"] = ft
        GCheckBox_791["fg"] = "#333333"
        GCheckBox_791["justify"] = "center"
        GCheckBox_791["text"] = self.v[11]
        GCheckBox_791.place(x=460,y=230,width=150,height=50)
        GCheckBox_791["offvalue"] = "1"
        GCheckBox_791["onvalue"] = "1"
        GCheckBox_791["command"] = self.GCheckBox_791_command

        GCheckBox_41=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_41["font"] = ft
        GCheckBox_41["fg"] = "#333333"
        GCheckBox_41["justify"] = "center"
        GCheckBox_41["text"] = self.v[12]
        GCheckBox_41.place(x=460,y=150,width=150,height=50)
        GCheckBox_41["offvalue"] = "1"
        GCheckBox_41["onvalue"] = "1"
        GCheckBox_41["command"] = self.GCheckBox_41_command






    def GCheckBox_265_command(self):
        if(self.call265 == 0):
            print("265")
            self.call265 += 1
            self.players += 1
            self.b.append(self.v[0])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_861_command(self):
        if(self.call861 == 0):
            print("861")
            self.call861 += 1
            self.players += 1
            self.b.append(self.v[1])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_653_command(self):
        if(self.call653 == 0):
            print("653")
            self.call653 += 1
            self.players += 1
            self.b.append(self.v[2])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_308_command(self):
        if(self.call308 == 0):
            print("308")
            self.call308 += 1
            self.players += 1
            self.b.append(self.v[3])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_194_command(self):
        if(self.call194 == 0):
            print("194")
            self.call194 += 1
            self.players += 1
            self.b.append(self.v[4])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_986_command(self):
        if(self.call986 == 0):
            print("986")
            self.call986 += 1
            self.players += 1
            self.b.append(self.v[5])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_680_command(self):
        if(self.call680 == 0):
            print("680")
            self.call680 += 1
            self.players += 1
            self.b.append(self.v[6])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_811_command(self):
        if(self.call811 == 0):
            print("811")
            self.call811 += 1
            self.players += 1
            self.b.append(self.v[7])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_845_command(self):
        if(self.call845 == 0):
            print("845")
            self.call845 += 1
            self.players += 1
            self.b.append(self.v[8])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_271_command(self):
        if(self.call271 == 0):
            print("271")
            self.call271 += 1
            self.players += 1
            self.b.append(self.v[9])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass
    def GCheckBox_794_command(self):
        if(self.call794 == 0):
            print("794")
            self.call794 += 1
            self.players += 1
            self.b.append(self.v[10])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_791_command(self):
        if(self.call791 == 0):
            print("791")
            self.call791 += 1
            self.players += 1
            self.b.append(self.v[11])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()

        else:
            pass
    def GCheckBox_41_command(self):
        if(self.call41 == 0):
            print("41")
            self.call41 += 1
            self.players += 1
            self.b.append(self.v[12])
        if(self.players == 11):
            root = tk.Tk()
            app = d(root,self.b,self.v)
            root.mainloop()
        else:
            pass

   


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root,v)
    root.mainloop()
