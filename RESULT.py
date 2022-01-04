import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root, team):
        self.team = team
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

        GMessage_957=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_957["font"] = ft
        GMessage_957["fg"] = "#333333"
        GMessage_957["justify"] = "center"
        GMessage_957["text"] = self.team +" "+ "won"
        GMessage_957.place(x=210,y=100,width=183,height=58)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
