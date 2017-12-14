from Tkinter import *
import time
import databs
import driver

def change_text(root,ilabel,text,ftext,iclr,fclr,spd): # function to change status and give update to the user what to do and what is happening
    ilabel.config(text=text,fg=iclr);
    root.update()
    time.sleep(spd)
    ilabel.config(text=ftext,fg=fclr);
    root.update()

def edit_connector(edit_box,ilabel,name,url,username,passwd,oldname):#old name to find the name to be fetched and changed in the database
    global userb
    if(not name or not url or not username or not passwd):
        change_text(edit_box,ilabel,'Please Fill All Entries ','Enter Details','red','white',1)
    else:
        inserted=databs.edit_entry(userb,name,url,username,passwd,oldname)
        if(inserted==0):
            change_text(edit_box,ilabel,'Error Occured.Please Try Again','Enter Details','red','white',1)
        else:
            main_box(inserted,edit_box)
def add_connector(addbox,ilabel,name,url,username,passwd):
    global userb

    if(not name or not url or not username or not passwd):
        change_text(addbox,ilabel,'Please Fill All Entries ','Enter Details','red','white',1)
    else:
        inserted=databs.new_entry(userb,name,url,username,passwd)
        if(inserted==0):
            change_text(addbox,ilabel,'Error Occured.Please Try Again','Enter Details','red','white',1)
        else:
            main_box(inserted,addbox)

def new_entry_box(details,master):
    master.destroy()
    addbox = Tk()
    addbox.config(bg="#404042")
    addbox.wm_title('Enter Details For New Site')

    ilabel=Label(addbox,text='Enter Details',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    ilabel.grid(row=0,column=0,padx=(10,0),pady=(5,5),columnspan=3)

    Label(addbox,text='Name',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=1,column=0,padx=(10,5),pady=(5,5))
    name=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    name.grid(row=1,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Url',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=2,column=0,padx=(10,5),pady=(5,5))
    url=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    url.grid(row=2,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Username/Email',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=3,column=0,padx=(10,5),pady=(5,5))
    use_name=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    use_name.grid(row=3,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=5,column=0,padx=(10,5),pady=(5,5))
    pass_wd=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    pass_wd.grid(row=5,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Button(addbox,text="Add",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:add_connector(addbox,ilabel,name.get(),url.get(),use_name.get(),pass_wd.get())).grid(row=6,column=0,columnspan=2,padx='10px',pady='5px')
    Button(addbox,text="Cancel",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:main_box(details,addbox)).grid(row=6,column=1,columnspan=2,padx='10px',pady='5px')


def edit_box(details,x,master):
    master.destroy()
    addbox = Tk()
    addbox.config(bg="#404042")
    addbox.wm_title('Enter Details For New Site')

    ilabel=Label(addbox,text='Enter Details',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    ilabel.grid(row=0,column=0,padx=(10,0),pady=(5,5),columnspan=3)

    Label(addbox,text='Name',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=1,column=0,padx=(10,5),pady=(5,5))
    name=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    name.insert(0,details[x][0])
    name.grid(row=1,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Url',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=2,column=0,padx=(10,5),pady=(5,5))
    url=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    url.insert(0,details[x][1])
    url.grid(row=2,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Username/Email',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=3,column=0,padx=(10,5),pady=(5,5))
    use_name=Entry(addbox,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    use_name.insert(0,details[x][2])
    use_name.grid(row=3,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    Label(addbox,text='Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=5,column=0,padx=(10,5),pady=(5,5))
    pass_wd=Entry(addbox,width=34,show="*",fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    pass_wd.grid(row=5,column=1,padx=(5,10),pady=(5,5),columnspan=2)
                                                                                                                                                                                            #details[x][0] is oldname
    Button(addbox,text="Edit",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:edit_connector(addbox,ilabel,name.get(),url.get(),use_name.get(),pass_wd.get(),details[x][0])).grid(row=6,column=0,columnspan=2,padx='10px',pady='5px')
    Button(addbox,text="Cancel",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:main_box(details,addbox)).grid(row=6,column=1,columnspan=2,padx='10px',pady='5px')

def main_box(details,*args):
    try:
        args[0].destroy()
    except:
        pass
    master = Tk()
    master.wm_title('Select Account')
    master.config(bg="#404042")
    Label(master,text='Name',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=0,column=0,padx='10px',pady='5px')
    Label(master,text='Username',fg="#ffffff",font="Tahoma 12 bold",bg="#404042").grid(row=0,column=2,padx='10px',pady='5px')
    Label(master,text='Actions',fg='#fff',font='Tahoma 12 bold',bg='#404042').grid(row=0,column=3,columnspan=2,padx='10px',pady='5px',sticky=W+E)
    for i in range(0,len(details)):
        for j in range(0,4):
            if(j%2==0):
                Label(master,text=details[i][j],fg="#ffffff",font="Tahoma 12",bg="#404042").grid(row=i+1,column=j,padx='10px',pady='5px')
        Button(master,text="Edit",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda x=i: edit_box(details,x,master)).grid(row=i+1,column=3,padx='10px',pady='5px')
        Button(master,text="Use",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda x=i: driver.auto_login(details[x][1],details[x][2],details[x][3])).grid(row=i+1,column=4,padx='10px',pady='5px')
    Button(master,text="Add",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:new_entry_box(details,master)).grid(row=i+2,column=0,columnspan=3,padx='10px',pady='5px')
    Button(master,text="Logout",relief=GROOVE,font="Tahoma 12",fg="white",bg="#404042",width=8,command=lambda:starter(master)).grid(row=i+2,column=3,columnspan=2,padx='10px',pady='5px')

def toggler(lab,btn): #Toggles Gui  b/w Login and Creator
    global check,root
    if(check==0):
        check=1
        lab.config(text="Log Into Your Account")
        btn.config(text="Create")
        root.update()
    elif(check==1):
        check=0
        lab.config(text="Create New Account")
        btn.config(text="Login")
        root.update()

def connector(user,passwd):  #if check == 0 Login and if check ==1 Create User
    global check ,root,ilabel,userb
    if(check==0):
        inserted=databs.log_in(user,passwd)
        if(inserted==0):
            change_text(root,ilabel,"Invalid Username Or Password",ftext,"red",fclr,1)
        else:
            change_text(root,ilabel,"Please wait.",'Please wait..',"#00cccc",fclr,1)
            change_text(root,ilabel,"Please wait..",'Logged In',"#00cccc",'#00cccc',1)
            userb=user
            root.destroy()
            main_box(inserted)
    elif(check==1):
        inserted=databs.new_user(user,passwd)
        if(inserted):
            change_text(root,ilabel,"User Created",ftext,"#00cccc",fclr,2)
        else:
            change_text(root,ilabel,"Failed.Invalid Username Or Password",ftext,"red",fclr,2)



def starter(*args):
    try:
        args[0].destroy()
    except:
        pass
    global root , ilabel
    root =Tk()
    root.configure(bg="#404042")
    root.wm_title("Please Login")

    #Creating cb button to switch b/w create user and login the application.
    cb_login=Button(root,text="Create New Account",relief=GROOVE,font="Tahoma 12 bold",width=20,fg="white",bg="#404042",command=lambda: toggler(cb_login,lgbtn))
    cb_login.grid(row=0,column=0,padx=5,pady=(0,10),columnspan=3,sticky=E+W)


    #creating login form
    ilabel=Label(root,text='Enter Username And Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    ilabel.grid(row=1,column=0,padx=(10,0),pady=(5,5),columnspan=3)

    usr_name=Label(root,text='Username',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    usr_name.grid(row=2,column=0,padx=(10,5),pady=(5,5))
    inp_name=Entry(root,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    inp_name.grid(row=2,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    usr_pass=Label(root,text='Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    usr_pass.grid(row=3,column=0,padx=(10,5),pady=(5,5))
    inp_pass=Entry(root,show="*",width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    inp_pass.grid(row=3,column=1,padx=(5,10),pady=(5,5),columnspan=2)

    lgbtn=Button(root,text="Login",relief=GROOVE,font="Tahoma 12 bold",width=8,fg="white",bg="#404042",command=lambda: connector(inp_name.get(),inp_pass.get()))
    lgbtn.grid(row=4,column=0,padx=0,pady=(5,10),columnspan=3)

    #login form created.
    root.mainloop()

check=0
root =0
fclr="white"
ftext="Enter Username and Password"
userb=0

#checks whether the to login or create new user.
#if 0 login if 1 then create account is used
starter()
