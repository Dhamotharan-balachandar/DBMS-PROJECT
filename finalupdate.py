import cx_Oracle
conn=cx_Oracle.connect('system/kannan@//localhost:1521/xe')
cur=conn.cursor()
import tkinter as tk 
from RESULT import App as w
class final:
    def __init__(self,b,v):
        self.b=b
        m,n,x,y=[],[],0,0
        u,p=0,0
        for i in self.b:
            m.append(i[0])
        self.v=v
        for i in self.v:
            n.append(i)
        for i in (0,22):
            if i%2==0:
                x=x+n[i]
            else:
                u=u+n[i]
        for i in (22,len(n) - 1):
            if i%2==1:
                y=y+n[i]
            else:
                p=p+n[i]
        if x>y:
            z=1
        else:
            z=0
        
            
        if z==1:
            for i in range (len(m)-11):
                a="update players set matches=matches+1,runs=runs+{},wicket=wicket+{},won=won+1 where p_id={}".format(n[i*2],n[i*2+1],m[i])
                print(a)
                cur.execute(a)
            conn.commit()
            l=0
        else:
            for i in range (len(m)-11):
                a="update players set matches=matches+1,runs=runs+{},wicket=wicket+{},lost=lost+1 where p_id={}".format(n[i*2],n[i*2+1],m[i])
                print(a)
                cur.execute(a)
            conn.commit()
            l=1
        if l==1:
            for i in range (11,len(m)):
                a="update players set matches=matches+1,runs=runs+{},wicket=wicket+{},won=won+1 where p_id={}".format(n[i*2],n[i*2+1],m[i])
                print(a)
                cur.execute(a)
            conn.commit()
        else:
            for i in range (11,len(m)):
                a="update players set matches=matches+1,runs=runs+{},wicket=wicket+{},lost=lost+1 where p_id={}".format(n[i*2],n[i*2+1],m[i])
                print(a)
                cur.execute(a)
            conn.commit()
        o=[]
        cur.execute ("select t_name from players where p_id={}".format(m[2]))
        for i in cur:
            o.append(i)
        print(o[0][0])
        e=o[0][0]
        cur.execute ("select t_name from players where p_id={}".format(m[13]))
        for i in cur:
            o.append(i)
        print(o[1][0])
        f=o[1][0]
        if e=='kkr' or f=='kkr':
            print('hi')
            if e=='kkr':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='kkr'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='kkr'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='kkr'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='kkr'".format(x,u))
            
        if e=='dc' or f=='dc':
            print('hi')
            if e=='dc':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='dc'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='dc'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='dc'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='dc'".format(x,u))
            
        if e=='mi' or f=='mi':
            print('hi')
            if e=='mi':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='mi'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='mi'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='mi'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='mi'".format(x,u))
            
        if e=='srh' or f=='srh':
            print('hi')
            if e=='srh':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='srh'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='srh'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='srh'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='srh'".format(x,u))
            
        if e=='rcb' or f=='rcb':
            print('hi')
            if e=='rcb':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='rcb'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='rcb'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='rcb'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='rcb'".format(x,u))
            
        if e=='csk' or f=='csk':
            print('hi')
            if e=='csk':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='csk'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='csk'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='csk'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='csk'".format(x,u))
            
        if e=='rr' or f=='rr':
            print('hi')
            if e=='rr':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='rr'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='rr'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='rr'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='rr'".format(x,u))
            
        if e=='pbks' or f=='pbks':
            print('hi')
            if e=='pbks':
                if x>y:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='pbks'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='pbks'".format(x,u))
            else:
                if y>x:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_won=t_won+1 where t_name='pbks'".format(x,u))
                else:
                    cur.execute("update teams set t_matches=t_matches+1,runs=runs+{},wickets=wickets+{},t_lost=t_lost+1 where t_name='pbks'".format(x,u))
            

        conn.commit()
        if(x > y):
            root = tk.Tk()
            app = w(root, e)
            root.mainloop()
        else:            
            root = tk.Tk()
            app = w(root, f)
            root.mainloop()




            
            




