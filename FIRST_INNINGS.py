import tkinter as tk
import tkinter.font as tkFont
from SECOND_INNINGS import App as f
class App:
    def __init__(self, root):
        #setting title
        root.title("MATCH")
        #setting window size
        width=601
        height=644
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_508=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_508["font"] = ft
        GLabel_508["fg"] = "#333333"
        GLabel_508["justify"] = "center"
        GLabel_508["text"] = "MATCH"
        GLabel_508.place(x=260,y=0,width=70,height=25)

        GLabel_808=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_808["font"] = ft
        GLabel_808["fg"] = "#333333"
        GLabel_808["justify"] = "center"
        GLabel_808["text"] = "1st INNINGS"
        GLabel_808.place(x=260,y=30,width=70,height=25)

        GMessage_894=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_894["font"] = ft
        GMessage_894["fg"] = "#333333"
        GMessage_894["justify"] = "center"
        GMessage_894["text"] = "Message"
        GMessage_894.place(x=0,y=110,width=150,height=44)

        GMessage_501=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_501["font"] = ft
        GMessage_501["fg"] = "#333333"
        GMessage_501["justify"] = "center"
        GMessage_501["text"] = "Message"
        GMessage_501.place(x=0,y=210,width=150,height=44)

        GMessage_310=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_310["font"] = ft
        GMessage_310["fg"] = "#333333"
        GMessage_310["justify"] = "center"
        GMessage_310["text"] = "Message"
        GMessage_310.place(x=0,y=460,width=150,height=44)

        GMessage_319=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_319["font"] = ft
        GMessage_319["fg"] = "#333333"
        GMessage_319["justify"] = "center"
        GMessage_319["text"] = "Message"
        GMessage_319.place(x=380,y=560,width=150,height=44)

        GMessage_967=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_967["font"] = ft
        GMessage_967["fg"] = "#333333"
        GMessage_967["justify"] = "center"
        GMessage_967["text"] = "Message"
        GMessage_967.place(x=0,y=310,width=150,height=44)

        GMessage_561=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_561["font"] = ft
        GMessage_561["fg"] = "#333333"
        GMessage_561["justify"] = "center"
        GMessage_561["text"] = "Message"
        GMessage_561.place(x=0,y=160,width=150,height=44)

        GMessage_405=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_405["font"] = ft
        GMessage_405["fg"] = "#333333"
        GMessage_405["justify"] = "center"
        GMessage_405["text"] = "Message"
        GMessage_405.place(x=0,y=560,width=150,height=44)

        GMessage_135=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_135["font"] = ft
        GMessage_135["fg"] = "#333333"
        GMessage_135["justify"] = "center"
        GMessage_135["text"] = "Message"
        GMessage_135.place(x=0,y=360,width=150,height=44)

        GMessage_506=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_506["font"] = ft
        GMessage_506["fg"] = "#333333"
        GMessage_506["justify"] = "center"
        GMessage_506["text"] = "Message"
        GMessage_506.place(x=380,y=110,width=150,height=44)

        GMessage_125=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_125["font"] = ft
        GMessage_125["fg"] = "#333333"
        GMessage_125["justify"] = "center"
        GMessage_125["text"] = "Message"
        GMessage_125.place(x=380,y=210,width=150,height=44)

        GMessage_696=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_696["font"] = ft
        GMessage_696["fg"] = "#333333"
        GMessage_696["justify"] = "center"
        GMessage_696["text"] = "Message"
        GMessage_696.place(x=380,y=460,width=150,height=44)

        GMessage_162=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_162["font"] = ft
        GMessage_162["fg"] = "#333333"
        GMessage_162["justify"] = "center"
        GMessage_162["text"] = "Message"
        GMessage_162.place(x=0,y=260,width=150,height=44)

        GMessage_314=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_314["font"] = ft
        GMessage_314["fg"] = "#333333"
        GMessage_314["justify"] = "center"
        GMessage_314["text"] = "Message"
        GMessage_314.place(x=0,y=410,width=150,height=44)

        GMessage_284=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_284["font"] = ft
        GMessage_284["fg"] = "#333333"
        GMessage_284["justify"] = "center"
        GMessage_284["text"] = "Message"
        GMessage_284.place(x=380,y=260,width=150,height=44)

        GMessage_778=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_778["font"] = ft
        GMessage_778["fg"] = "#333333"
        GMessage_778["justify"] = "center"
        GMessage_778["text"] = "Message"
        GMessage_778.place(x=380,y=60,width=150,height=44)

        GMessage_923=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_923["font"] = ft
        GMessage_923["fg"] = "#333333"
        GMessage_923["justify"] = "center"
        GMessage_923["text"] = "Message"
        GMessage_923.place(x=380,y=160,width=150,height=44)

        GMessage_404=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_404["font"] = ft
        GMessage_404["fg"] = "#333333"
        GMessage_404["justify"] = "center"
        GMessage_404["text"] = "Message"
        GMessage_404.place(x=380,y=360,width=150,height=44)

        GMessage_448=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_448["font"] = ft
        GMessage_448["fg"] = "#333333"
        GMessage_448["justify"] = "center"
        GMessage_448["text"] = "Message"
        GMessage_448.place(x=380,y=310,width=150,height=44)

        GMessage_904=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_904["font"] = ft
        GMessage_904["fg"] = "#333333"
        GMessage_904["justify"] = "center"
        GMessage_904["text"] = "Message"
        GMessage_904.place(x=380,y=410,width=150,height=44)

        GMessage_919=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_919["font"] = ft
        GMessage_919["fg"] = "#333333"
        GMessage_919["justify"] = "center"
        GMessage_919["text"] = "Message"
        GMessage_919.place(x=380,y=510,width=150,height=44)

        GLineEdit_813=tk.Entry(root)
        GLineEdit_813["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_813["font"] = ft
        GLineEdit_813["fg"] = "#333333"
        GLineEdit_813["justify"] = "center"
        GLineEdit_813["text"] = ""
        GLineEdit_813.place(x=130,y=120,width=70,height=25)

        GLineEdit_794=tk.Entry(root)
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=130,y=170,width=70,height=25)

        GLineEdit_896=tk.Entry(root)
        GLineEdit_896["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_896["font"] = ft
        GLineEdit_896["fg"] = "#333333"
        GLineEdit_896["justify"] = "center"
        GLineEdit_896["text"] = ""
        GLineEdit_896.place(x=130,y=270,width=70,height=25)

        GLineEdit_361=tk.Entry(root)
        GLineEdit_361["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_361["font"] = ft
        GLineEdit_361["fg"] = "#333333"
        GLineEdit_361["justify"] = "center"
        GLineEdit_361["text"] = ""
        GLineEdit_361.place(x=130,y=220,width=70,height=25)

        GLineEdit_962=tk.Entry(root)
        GLineEdit_962["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_962["font"] = ft
        GLineEdit_962["fg"] = "#333333"
        GLineEdit_962["justify"] = "center"
        GLineEdit_962["text"] = ""
        GLineEdit_962.place(x=510,y=220,width=70,height=25)

        GLineEdit_426=tk.Entry(root)
        GLineEdit_426["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_426["font"] = ft
        GLineEdit_426["fg"] = "#333333"
        GLineEdit_426["justify"] = "center"
        GLineEdit_426["text"] = ""
        GLineEdit_426.place(x=510,y=120,width=70,height=25)

        GLineEdit_482=tk.Entry(root)
        GLineEdit_482["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_482["font"] = ft
        GLineEdit_482["fg"] = "#333333"
        GLineEdit_482["justify"] = "center"
        GLineEdit_482["text"] = ""
        GLineEdit_482.place(x=130,y=420,width=70,height=25)

        GLineEdit_443=tk.Entry(root)
        GLineEdit_443["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_443["font"] = ft
        GLineEdit_443["fg"] = "#333333"
        GLineEdit_443["justify"] = "center"
        GLineEdit_443["text"] = ""
        GLineEdit_443.place(x=510,y=270,width=70,height=25)

        GLineEdit_953=tk.Entry(root)
        GLineEdit_953["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_953["font"] = ft
        GLineEdit_953["fg"] = "#333333"
        GLineEdit_953["justify"] = "center"
        GLineEdit_953["text"] = ""
        GLineEdit_953.place(x=130,y=570,width=70,height=25)

        GLineEdit_853=tk.Entry(root)
        GLineEdit_853["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_853["font"] = ft
        GLineEdit_853["fg"] = "#333333"
        GLineEdit_853["justify"] = "center"
        GLineEdit_853["text"] = ""
        GLineEdit_853.place(x=510,y=70,width=70,height=25)

        GLineEdit_254=tk.Entry(root)
        GLineEdit_254["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_254["font"] = ft
        GLineEdit_254["fg"] = "#333333"
        GLineEdit_254["justify"] = "center"
        GLineEdit_254["text"] = ""
        GLineEdit_254.place(x=510,y=170,width=70,height=25)

        GLineEdit_954=tk.Entry(root)
        GLineEdit_954["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_954["font"] = ft
        GLineEdit_954["fg"] = "#333333"
        GLineEdit_954["justify"] = "center"
        GLineEdit_954["text"] = ""
        GLineEdit_954.place(x=510,y=320,width=70,height=25)

        GLineEdit_326=tk.Entry(root)
        GLineEdit_326["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_326["font"] = ft
        GLineEdit_326["fg"] = "#333333"
        GLineEdit_326["justify"] = "center"
        GLineEdit_326["text"] = ""
        GLineEdit_326.place(x=130,y=370,width=70,height=25)

        GLineEdit_871=tk.Entry(root)
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "center"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=130,y=320,width=70,height=25)

        GLineEdit_104=tk.Entry(root)
        GLineEdit_104["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_104["font"] = ft
        GLineEdit_104["fg"] = "#333333"
        GLineEdit_104["justify"] = "center"
        GLineEdit_104["text"] = ""
        GLineEdit_104.place(x=510,y=420,width=70,height=25)

        GLineEdit_701=tk.Entry(root)
        GLineEdit_701["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_701["font"] = ft
        GLineEdit_701["fg"] = "#333333"
        GLineEdit_701["justify"] = "center"
        GLineEdit_701["text"] = ""
        GLineEdit_701.place(x=510,y=370,width=70,height=25)

        GLineEdit_755=tk.Entry(root)
        GLineEdit_755["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_755["font"] = ft
        GLineEdit_755["fg"] = "#333333"
        GLineEdit_755["justify"] = "center"
        GLineEdit_755["text"] = ""
        GLineEdit_755.place(x=130,y=470,width=70,height=25)

        GLineEdit_195=tk.Entry(root)
        GLineEdit_195["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_195["font"] = ft
        GLineEdit_195["fg"] = "#333333"
        GLineEdit_195["justify"] = "center"
        GLineEdit_195["text"] = ""
        GLineEdit_195.place(x=510,y=470,width=70,height=25)

        GLineEdit_481=tk.Entry(root)
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "center"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=510,y=570,width=70,height=25)

        GLineEdit_393=tk.Entry(root)
        GLineEdit_393["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_393["font"] = ft
        GLineEdit_393["fg"] = "#333333"
        GLineEdit_393["justify"] = "center"
        GLineEdit_393["text"] = ""
        GLineEdit_393.place(x=510,y=520,width=70,height=25)


        GMessage_47=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_47["font"] = ft
        GMessage_47["fg"] = "#333333"
        GMessage_47["justify"] = "center"
        GMessage_47["text"] = "Batting"
        GMessage_47.place(x=80,y=30,width=80,height=25)

        GMessage_75=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_75["font"] = ft
        GMessage_75["fg"] = "#333333"
        GMessage_75["justify"] = "center"
        GMessage_75["text"] = "Bowling"
        GMessage_75.place(x=450,y=30,width=94,height=30)

        GMessage_454=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_454["font"] = ft
        GMessage_454["fg"] = "#333333"
        GMessage_454["justify"] = "center"
        GMessage_454["text"] = "Message"
        GMessage_454.place(x=0,y=60,width=150,height=44)

        GLineEdit_809=tk.Entry(root)
        GLineEdit_809["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_809["font"] = ft
        GLineEdit_809["fg"] = "#333333"
        GLineEdit_809["justify"] = "center"
        GLineEdit_809["text"] = ""
        GLineEdit_809.place(x=130,y=70,width=70,height=25)

        GMessage_716=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_716["font"] = ft
        GMessage_716["fg"] = "#333333"
        GMessage_716["justify"] = "center"
        GMessage_716["text"] = "Message"
        GMessage_716.place(x=0,y=510,width=150,height=44)

        GButton_706=tk.Button(root)
        GButton_706["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_706["font"] = ft
        GButton_706["fg"] = "#000000"
        GButton_706["justify"] = "center"
        GButton_706["text"] = "FINISH"
        GButton_706.place(x=270,y=610,width=70,height=25)
        GButton_706["command"] = self.GButton_706_command

        GLineEdit_722=tk.Entry(root)
        GLineEdit_722["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_722["font"] = ft
        GLineEdit_722["fg"] = "#333333"
        GLineEdit_722["justify"] = "center"
        GLineEdit_722["text"] = ""
        GLineEdit_722.place(x=130,y=520,width=70,height=25)

    def GButton_706_command(self):
        root = tk.Tk()
        app = f(root)
        root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()