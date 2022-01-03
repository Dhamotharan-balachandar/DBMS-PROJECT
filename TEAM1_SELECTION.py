import tkinter as tk
import tkinter.font as tkFont
from TEAM2_SELECTION import App as d
class App:
    def __init__(self, root):
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
        GCheckBox_265["text"] = "CheckBox"
        GCheckBox_265.place(x=10,y=150,width=150,height=50)
        GCheckBox_265["offvalue"] = "0"
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
        GCheckBox_861["text"] = "CheckBox"
        GCheckBox_861.place(x=10,y=310,width=150,height=50)
        GCheckBox_861["offvalue"] = "0"
        GCheckBox_861["onvalue"] = "1"
        GCheckBox_861["command"] = self.GCheckBox_861_command

        GCheckBox_653=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_653["font"] = ft
        GCheckBox_653["fg"] = "#333333"
        GCheckBox_653["justify"] = "center"
        GCheckBox_653["text"] = "CheckBox"
        GCheckBox_653.place(x=460,y=310,width=150,height=50)
        GCheckBox_653["offvalue"] = "0"
        GCheckBox_653["onvalue"] = "1"
        GCheckBox_653["command"] = self.GCheckBox_653_command

        GCheckBox_308=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_308["font"] = ft
        GCheckBox_308["fg"] = "#333333"
        GCheckBox_308["justify"] = "center"
        GCheckBox_308["text"] = "CheckBox"
        GCheckBox_308.place(x=250,y=390,width=150,height=50)
        GCheckBox_308["offvalue"] = "0"
        GCheckBox_308["onvalue"] = "1"
        GCheckBox_308["command"] = self.GCheckBox_308_command

        GCheckBox_194=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_194["font"] = ft
        GCheckBox_194["fg"] = "#333333"
        GCheckBox_194["justify"] = "center"
        GCheckBox_194["text"] = "CheckBox"
        GCheckBox_194.place(x=250,y=150,width=150,height=50)
        GCheckBox_194["offvalue"] = "0"
        GCheckBox_194["onvalue"] = "1"
        GCheckBox_194["command"] = self.GCheckBox_194_command

        GCheckBox_986=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_986["font"] = ft
        GCheckBox_986["fg"] = "#333333"
        GCheckBox_986["justify"] = "center"
        GCheckBox_986["text"] = "CheckBox"
        GCheckBox_986.place(x=10,y=230,width=150,height=50)
        GCheckBox_986["offvalue"] = "0"
        GCheckBox_986["onvalue"] = "1"
        GCheckBox_986["command"] = self.GCheckBox_986_command

        GCheckBox_680=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_680["font"] = ft
        GCheckBox_680["fg"] = "#333333"
        GCheckBox_680["justify"] = "center"
        GCheckBox_680["text"] = "CheckBox"
        GCheckBox_680.place(x=460,y=70,width=150,height=50)
        GCheckBox_680["offvalue"] = "0"
        GCheckBox_680["onvalue"] = "1"
        GCheckBox_680["command"] = self.GCheckBox_680_command

        GCheckBox_811=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_811["font"] = ft
        GCheckBox_811["fg"] = "#333333"
        GCheckBox_811["justify"] = "center"
        GCheckBox_811["text"] = "CheckBox"
        GCheckBox_811.place(x=250,y=310,width=150,height=50)
        GCheckBox_811["offvalue"] = "0"
        GCheckBox_811["onvalue"] = "1"
        GCheckBox_811["command"] = self.GCheckBox_811_command

        GCheckBox_845=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_845["font"] = ft
        GCheckBox_845["fg"] = "#333333"
        GCheckBox_845["justify"] = "center"
        GCheckBox_845["text"] = "CheckBox"
        GCheckBox_845.place(x=250,y=230,width=150,height=50)
        GCheckBox_845["offvalue"] = "0"
        GCheckBox_845["onvalue"] = "1"
        GCheckBox_845["command"] = self.GCheckBox_845_command

        GCheckBox_271=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_271["font"] = ft
        GCheckBox_271["fg"] = "#333333"
        GCheckBox_271["justify"] = "center"
        GCheckBox_271["text"] = "CheckBox"
        GCheckBox_271.place(x=10,y=70,width=150,height=50)
        GCheckBox_271["offvalue"] = "0"
        GCheckBox_271["onvalue"] = "1"
        GCheckBox_271["command"] = self.GCheckBox_271_command

        GCheckBox_794=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_794["font"] = ft
        GCheckBox_794["fg"] = "#333333"
        GCheckBox_794["justify"] = "center"
        GCheckBox_794["text"] = "CheckBox"
        GCheckBox_794.place(x=250,y=70,width=150,height=50)
        GCheckBox_794["offvalue"] = "0"
        GCheckBox_794["onvalue"] = "1"
        GCheckBox_794["command"] = self.GCheckBox_794_command

        GCheckBox_791=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_791["font"] = ft
        GCheckBox_791["fg"] = "#333333"
        GCheckBox_791["justify"] = "center"
        GCheckBox_791["text"] = "CheckBox"
        GCheckBox_791.place(x=460,y=230,width=150,height=50)
        GCheckBox_791["offvalue"] = "0"
        GCheckBox_791["onvalue"] = "1"
        GCheckBox_791["command"] = self.GCheckBox_791_command

        GCheckBox_41=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_41["font"] = ft
        GCheckBox_41["fg"] = "#333333"
        GCheckBox_41["justify"] = "center"
        GCheckBox_41["text"] = "CheckBox"
        GCheckBox_41.place(x=460,y=150,width=150,height=50)
        GCheckBox_41["offvalue"] = "0"
        GCheckBox_41["onvalue"] = "1"
        GCheckBox_41["command"] = self.GCheckBox_41_command

        GCheckBox_653=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_653["font"] = ft
        GCheckBox_653["fg"] = "#333333"
        GCheckBox_653["justify"] = "center"
        GCheckBox_653["text"] = "CheckBox"
        GCheckBox_653.place(x=460,y=310,width=150,height=50)
        GCheckBox_653["offvalue"] = "0"
        GCheckBox_653["onvalue"] = "1"
        GCheckBox_653["command"] = self.GCheckBox_653_command

        GCheckBox_962=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_962["font"] = ft
        GCheckBox_962["fg"] = "#333333"
        GCheckBox_962["justify"] = "center"
        GCheckBox_962["text"] = "CheckBox"
        GCheckBox_962.place(x=10,y=390,width=150,height=50)
        GCheckBox_962["offvalue"] = "0"
        GCheckBox_962["onvalue"] = "1"
        GCheckBox_962["command"] = self.GCheckBox_962_command

        GCheckBox_117=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_117["font"] = ft
        GCheckBox_117["fg"] = "#333333"
        GCheckBox_117["justify"] = "center"
        GCheckBox_117["text"] = "CheckBox"
        GCheckBox_117.place(x=460,y=390,width=150,height=50)
        GCheckBox_117["offvalue"] = "0"
        GCheckBox_117["onvalue"] = "1"
        GCheckBox_117["command"] = self.GCheckBox_117_command

        GButton_192=tk.Button(root)
        GButton_192["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_192["font"] = ft
        GButton_192["fg"] = "#c13535"
        GButton_192["justify"] = "center"
        GButton_192["text"] = "FINISH"
        GButton_192.place(x=300,y=560,width=70,height=25)
        GButton_192["command"] = self.GButton_192_command



    def GCheckBox_265_command(self):
        print("command")


    def GCheckBox_861_command(self):
        print("command")


    def GCheckBox_653_command(self):
        print("command")


    def GCheckBox_308_command(self):
        print("command")


    def GCheckBox_194_command(self):
        print("command")


    def GCheckBox_986_command(self):
        print("command")


    def GCheckBox_680_command(self):
        print("command")


    def GCheckBox_811_command(self):
        print("command")


    def GCheckBox_845_command(self):
        print("command")


    def GCheckBox_271_command(self):
        print("command")


    def GCheckBox_794_command(self):
        print("command")


    def GCheckBox_791_command(self):
        print("command")


    def GCheckBox_41_command(self):
        print("command")


    def GCheckBox_653_command(self):
        print("command")


    def GCheckBox_962_command(self):
        print("command")


    def GCheckBox_117_command(self):
        print("command")

    def GButton_192_command(self):
        root = tk.Tk()
        app = d(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
