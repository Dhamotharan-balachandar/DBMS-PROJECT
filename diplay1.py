import cx_Oracle
from tkinter import *
class dis:
    def __init__(self,root,cur,num):
        root.title('Details')
        root.geometry('600x600+100+100')
        t=Text(root)
        t.place(x=30,y=30)
        a=[]
        b=['Player id:','Name:','Number of matches:','won:','Lost:','Wickets:','Runs:','Team name:']
        for i in cur :
            a.append(i)
        for i in range(105) :
            if a[i][0]==num:
                break
        for j in range(8):
            m=b[j]+str(a[i][j])
            t.insert(END,m)
            t.insert(END,'\n')

root=Tk()
root.mainloop()

