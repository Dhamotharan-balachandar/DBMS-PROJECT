from tkinter import *
import cx_Oracle
conn=cx_Oracle.connect('system/kannan@//localhost:1521/xe')
cr = conn.cursor()
class table:
    def __init__(self,root):
        root.title('Details')
        root.geometry('600x600+100+100')
        cr.execute("select * from teams order by t_won desc, runs desc")
        t=Text(root)
        t.insert(END,'Name   Matches    Won    Lost    Runs    Wickets\n')
        t.place(x=20,y=20)
        for i in cr:
            for j in range (0,6):
                t.insert(END,i[j])
                t.insert(END,'\t')
            t.insert(END,'\n')
        

root=Tk()
root.mainloop()
