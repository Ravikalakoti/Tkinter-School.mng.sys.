from tkinter import *
from tkinter import messagebox
from dbinfor import*
from tkinter import ttk
from datetime import datetime
create_table()

win=Tk()
win.state("zoomed")
win.configure(bg="yellow")
win.title("vidya mandir")
win.resizable(width=False ,height=False)

lbl_title=Label(win,text="Students Management system",font=('',35,'bold'),bg='yellow',fg='blue')
lbl_title.pack()

def due_amt_db(e):
    sid=int(e.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select course_fee,amount from students where stu_id=%a",(sid,))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("balance","Student does not exist on this id")
    else:   
        messagebox.showinfo("Balance",f"Due Amount : {row[0]-row[1]}")    
    con.close()

def deposit_fee_db(e1,e2):
    sid=int(e1.get())
    amt=int(e2.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select course_fee,amount from students where stu_id=%s",(sid,))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("Fee Deposit",'Student does not exist on this id')
    else:
        if(row[1]<row[0]):
            if(row[0]>=(amt+row[1])):
                cur.execute("update students set amount=amount+%s where stu_id=%s",(amt,sid))
                messagebox.showinfo("Fee Deposit",'Fee Deposited')
                con.commit()
            else:
                messagebox.showinfo("Fee Deposit",'Deposited amount is not valid')
        else:
            messagebox.showwarning("Fee Deposit",'Already fullpaid')
    con.close()

def update_stu_db(e1,e2,e3,e4,e5):
    sid=e1.get()
    name=e2.get()
    mob=e3.get()
    email=e4.get()
    course=e5.get()
    print(sid,name,mob,email,course)
    con=getcon()
    cur=con.cursor()
    cur.execute("""update students set stu_name=%s, stu_mob=%s, stu_email=%s, stu_course=%s where stu_id=%s""",(name,mob,email,course,sid))
    con.commit()
    con.close()
    messagebox.showinfo("Update Student","Student Record Updated...")

def search_stu_db(frm,e):
    sid=int(e.get())
    con=getcon()
    cur=con.cursor()
    cur.execute("select stu_name,stu_mob,stu_course,amount from students where stu_id=%s",(sid,))
    row=cur.fetchone()
    if(row==None):
        messagebox.showwarning("Student Search","Student Id does not exit")
    else:
        details="Name\tMobile\t\tcourse\t\tamount\n"
        details=details+f"{str(row[0])}\t{row[1]}\t{row[2]}\t{row[3]}"
        messagebox.showinfo("Student Search",details)
        option=messagebox.askyesno("Update Student", message="Do you want to update student?")
        if(option==True):
            updatescreen(frm,sid)
    
    
  
      

def logout(frm):
	frm.destroy()
	Homescreen()
	
def reg_db(e1,e2,e3,e4,e5,e6):
    name=e1.get()
    mob=e2.get()
    email=e3.get()
    course=e4.get()
    fee=int(e5.get())
    amount=int(e6.get())
    dt=datetime.now().date()
    sid=getnextid()
    con=getcon()
    cur=con.cursor()
    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(sid,name,mob,email,course,dt,fee,amount))
    con.commit()
    messagebox.showinfo('Student Reg',f'Student Registered Successfully With Id:{sid} ')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e1.focus()
        
        
        
        
        
        

def reset(frm,x1,x2):
	x1.delete(0,END)
	x2.delete(0,END)
	x1.focus()


def login(frm,x1,x2):
	u=x1.get()
	p=x2.get()
	if (len(u)==0 or len(p)==0):
		messagebox.showwarning('warning','user name and pasword can not be empty')
	else:
		if (u=='ravi' and p=='ravi'):
			messagebox.showinfo('sucess','welcome admin')
			frm.destroy()
			welcomescreen()
		else:
			messagebox.showerror('error','invalid user name or password')

def back(frm):
        frm.destroy()
        welcomescreen()



def registerscreen(wfrm):
        wfrm.destroy()
        frm=Frame(win,bg='blue')
        frm.place(x=0,y=100,relwidth=1,relheight=1)

        lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
        lbl_welcome.place(x=10,y=10)

        btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=5)
        btn_logout.place(relx=0.93,y=11)

        btn_back=Button(frm,text='Back',command=lambda:back(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=5)
        btn_back.place(relx=0.84,y=11)

        lbl_name=Label(frm,text='Student Name:',font=('',20,'bold'),bg='blue')
        lbl_name.place(relx=0.3,rely=0.1)
        entry_name=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_name.place(relx=0.47,rely=0.1)
        entry_name.focus()

        lbl_mob=Label(frm,text='Student mob:',font=('',20,'bold'),bg='blue')
        lbl_mob.place(relx=0.3,rely=0.2)
        entry_mob=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_mob.place(relx=0.47,rely=0.2)

        lbl_email=Label(frm,text='Student Email:',font=('',20,'bold'),bg='blue')
        lbl_email.place(relx=0.3,rely=0.3)
        entry_email=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_email.place(relx=0.47,rely=0.3)

        lbl_course=Label(frm,text='Course Name:',font=('',20,'bold'),bg='blue')
        lbl_course.place(relx=0.3,rely=0.4)
        entry_course=ttk.Combobox(frm,values=["Python","python+Django","Python+Ml","Python+Ai"],font=('',14,'bold'))
        entry_course.place(relx=0.47,rely=0.4)

        lbl_fee=Label(frm,text='Course Fee:',font=('',20,'bold'),bg='blue')
        lbl_fee.place(relx=0.3,rely=0.50)
        entry_fee=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_fee.place(relx=0.47,rely=0.5)  
                        
        lbl_amt=Label(frm,text='Amount:',font=('',20,'bold'),bg='blue')
        lbl_amt.place(relx=0.3,rely=0.6)
        entry_amt=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_amt.place(relx=0.47,rely=0.6)                

        btn_reg=Button(frm,text='Register',command=lambda:reg_db(entry_name,entry_mob,entry_email,entry_course,entry_fee,entry_amt),font=('',15,'bold'),bd=5,width=7,bg='green',fg='yellow')
        btn_reg.place(relx=0.48,rely=0.69)

        btn_reset=Button(frm,text='Reset',font=('',15,'bold'),bd=5,width=7,bg='green',fg='yellow')
        btn_reset.place(relx=0.57,rely=0.69)

def depositscreen(wfrm):
        wfrm.destroy()
        frm=Frame(win,bg='blue')
        frm.place(x=0,y=100,relwidth=1,relheight=1)

        lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
        lbl_welcome.place(x=10,y=10)

        btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=6)
        btn_logout.place(relx=0.92,y=11)

        btn_back=Button(frm,text='Back',command=lambda:back(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=5)
        btn_back.place(relx=0.84,y=11)

        lbl_sid=Label(frm,text='Student Id:',font=('',20,'bold'),bg='blue')
        lbl_sid.place(relx=0.3,rely=0.1)
        entry_sid=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_sid.place(relx=0.47,rely=0.1)
        entry_sid.focus()

        lbl_amt=Label(frm,text='Amount:',font=('',20,'bold'),bg='blue')
        lbl_amt.place(relx=0.3,rely=0.2)
        entry_amt=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_amt.place(relx=0.47,rely=0.2)
        entry_amt.focus()

        btn_dep=Button(frm,text='Deposit',command=lambda:deposit_fee_db(entry_sid,entry_amt),font=('',15,'bold'),bd=5,width=7,bg='green',fg='yellow')
        btn_dep.place(relx=0.48,rely=0.3)
    
        btn_reset=Button(frm,text='Reset',command=lambda:reset(frm,entry_sid,entry_amt),font=('',15,'bold'),bd=5,bg='green',fg='yellow',width=8)
        btn_reset.place(relx=0.58,rely=0.3)


def updatescreen(wfrm,sid):
        wfrm.destroy()
        frm=Frame(win,bg='blue')
        frm.place(x=0,y=100,relwidth=1,relheight=1)

        lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
        lbl_welcome.place(x=10,y=10)

        btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=5)
        btn_logout.place(relx=0.93,y=11)

        btn_back=Button(frm,text='Back',command=lambda:back(frm),font=('',14,'bold'),bg='green',fg='yellow',bd=5,width=5)
        btn_back.place(relx=0.84,y=11)

        lbl_name=Label(frm,text='Student Name:',font=('',20,'bold'),bg='blue')
        lbl_name.place(relx=0.3,rely=0.1)
        entry_name=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_name.place(relx=0.47,rely=0.1)
        entry_name.focus()

        lbl_mob=Label(frm,text='Student mob:',font=('',20,'bold'),bg='blue')
        lbl_mob.place(relx=0.3,rely=0.2)
        entry_mob=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_mob.place(relx=0.47,rely=0.2)

        lbl_email=Label(frm,text='Student Email:',font=('',20,'bold'),bg='blue')
        lbl_email.place(relx=0.3,rely=0.3)
        entry_email=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_email.place(relx=0.47,rely=0.3)

        lbl_course=Label(frm,text='Course Name:',font=('',20,'bold'),bg='blue')
        lbl_course.place(relx=0.3,rely=0.4)
        entry_course=ttk.Combobox(frm,values=["Python","python+Django","Python+Ml","Python+Ai"],font=('',14,'bold'))
        entry_course.place(relx=0.47,rely=0.4)

        lbl_fee=Label(frm,text='Course Fee:',font=('',20,'bold'),bg='blue')
        lbl_fee.place(relx=0.3,rely=0.50)
        entry_fee=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_fee.place(relx=0.47,rely=0.5)  
                        
        lbl_amt=Label(frm,text='Amount:',font=('',20,'bold'),bg='blue')
        lbl_amt.place(relx=0.3,rely=0.6)
        entry_amt=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
        entry_amt.place(relx=0.47,rely=0.6)                

        btn_reg=Button(frm,text='Register',command=lambda:reg_db(entry_name,entry_mob,entry_email,entry_course,entry_fee,entry_amt),font=('',15,'bold'),bd=5,width=7,bg='green',fg='yellow')
        btn_reg.place(relx=0.48,rely=0.69)

        btn_reset=Button(frm,text='Reset',font=('',15,'bold'),bd=5,width=7,bg='green',fg='yellow')
        btn_reset.place(relx=0.57,rely=0.69)
   


def searchscreen(wfrm):
    wfrm.destroy()
    frm=Frame(win,bg='blue')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
    lbl_welcome.place(x=10,y=10)

    btn_logout=Button(frm,command=lambda:logout(frm),text='logout',font=('',15,'bold'),bg='green',fg='yellow',bd=5,width=8)
    btn_logout.place(relx=.9,y=10)

    btn_back=Button(frm,command=lambda:back(frm),text='back',font=('',15,'bold'),bg='green',fg='yellow',bd=5,width=8)
    btn_back.place(x=10,y=50)

    lbl_name=Label(frm,text='Student Id:',font=('',20,'bold'),bg='blue')
    lbl_name.place(relx=.3,rely=.1)
    entry_name=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
    entry_name.place(relx=.42,rely=.1)
    entry_name.focus()

    
    btn_sear=Button(frm,text='Search',command=lambda:search_stu_db(frm,entry_name),font=('',15,'bold'),bg='green',fg='yellow',bd=5,width=8)
    btn_sear.place(relx=.4,rely=.2)

    btn_reset=Button(frm,text='reset',font=('',15,'bold'),bd=5,width=8,bg='green',fg='yellow')
    btn_reset.place(relx=.51,rely=.2)

def dueamountscreen(wfrm):
    wfrm.destroy()
    frm=Frame(win,bg='blue')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
    lbl_welcome.place(x=10,y=10)

    btn_logout=Button(frm,command=lambda:logout(frm),text='logout',font=('',15,'bold'),bd=5,bg='green',fg='yellow',width=8)
    btn_logout.place(relx=.9,y=10)

    btn_back=Button(frm,command=lambda:back(frm),text='back',font=('',15,'bold'),bd=5,bg='green',fg='yellow',width=8)
    btn_back.place(x=10,y=50)

    lbl_name=Label(frm,text='Student Id:',font=('',20,'bold'),bg='blue')
    lbl_name.place(relx=.3,rely=.1)
    entry_sid=Entry(frm,font=('',15,'bold'),bd=5,bg='yellow')
    entry_sid.place(relx=.47,rely=.1)
    entry_sid.focus()
   
    btn_sub=Button(frm,text='Submit',command=lambda:due_amt_db(entry_sid),font=('',15,'bold'),bd=5,bg='green',fg='yellow',width=8)
    btn_sub.place(relx=.4,rely=.2)

    btn_reset=Button(frm,text='Reset',font=('',15,'bold'),bd=5,bg='green',fg='yellow',width=8)
    btn_reset.place(relx=.55,rely=.2)    

    
def welcomescreen():
    frm=Frame(win,bg='blue')
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    lbl_welcome=Label(frm,text='Welcome:Admin',font=('',20,'bold'),bg='blue',fg='yellow')
    lbl_welcome.place(x=10,y=10)

    btn_logout=Button(frm,text='Logout',command=lambda:logout(frm),font=('',15,'bold'),bg='green',fg='yellow',bd=5,width=6)
    btn_logout.place(relx=0.9,y=10)

    btn_reg=Button(frm,text="Register New Student",command=lambda:registerscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_reg.place(relx=0.4,y=90)

    btn_search=Button(frm,text="Search Student",command=lambda:searchscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_search.place(relx=0.4,y=190)

    btn_update=Button(frm,text="Deposit Fee",command=lambda:depositscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_update.place(relx=0.4,y=290)

    btn_due=Button(frm,text="Due Amount",command=lambda:dueamountscreen(frm),font=('',20,'bold'),bg='green',bd=6,width=18)
    btn_due.place(relx=0.4,y=390)

    
    
def Homescreen():
    frm=Frame(win,bg='blue')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    lbl_user=Label(frm,text='Username:',font=('',20,'bold'),bg='blue',fg='red')
    lbl_user.place(x=400,y=100)

    lbl_pass=Label(frm,text='Password:',font=('',20,'bold'),bg='blue',fg='red')
    lbl_pass.place(x=400,y=160)

    entry_user=Entry(frm,font=('',15,'bold'),bg='yellow')
    entry_user.place(x=560,y=100)
    entry_user.focus()

    entry_pass=Entry(frm,font=('',15,'bold'),show='*',bg='yellow')
    entry_pass.place(x=560,y=160)

    btn_login=Button(frm,text='Login',command=lambda:login(frm,entry_user,entry_pass),font=('',15,'bold'),width=6,bd=1,bg='green',fg='yellow')
    btn_login.place(x=570,y=200)

    btn_reset=Button(frm,text='Reset',command=lambda:reset(frm,entry_user,entry_pass),font=('',15,'bold'),width=6,bd=1,bg='green',fg='yellow')
    btn_reset.place(x=680,y=200)




    

    


    
Homescreen()
win.mainloop()
