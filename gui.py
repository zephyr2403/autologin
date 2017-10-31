from Tkinter import *
def starter():
    root =Tk()
    root.configure(bg="#404042")

    #Creating cb button to switch b/w create user and login the application.
    cb_login=Button(root,text="Log Into Your Account",relief=GROOVE,font="Tahoma 12 bold",width=20,fg="white",bg="#404042")
    cb_login.grid(row=0,column=0,padx=0,pady=(0,10),columnspan=2)
    cb_create=Button(root,text="Create User",relief=GROOVE,font="Tahoma 12 bold",width=20,fg="white",bg="#404042")
    cb_create.grid(row=0,column=2,padx=0,pady=(0,10))

    #creating login form
    ilabel=Label(root,text='Enter Username And Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    ilabel.grid(row=1,column=0,padx=(10,0),pady=(5,5),columnspan=3)

    usr_name=Label(root,text='Username',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    usr_name.grid(row=2,column=0,padx=(10,0),pady=(5,5))
    inp_name=Entry(root,width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    inp_name.grid(row=2,column=1,padx=(0,10),pady=(5,5),columnspan=2)

    usr_pass=Label(root,text='Password',fg="#ffffff",font="Tahoma 12 bold",bg="#404042")
    usr_pass.grid(row=3,column=0,padx=(10,0),pady=(5,5))
    inp_pass=Entry(root,show="*",width=34,fg="white",bg="#404042",borderwidth=3,font="Tahoma 12",insertbackground="white")
    inp_pass.grid(row=3,column=1,padx=(0,10),pady=(5,5),columnspan=2)

    lgbtn=Button(root,text="Login",relief=GROOVE,font="Tahoma 12 bold",width=8,fg="white",bg="#404042")
    lgbtn.grid(row=4,column=0,padx=0,pady=(5,10),columnspan=3,)

    root.mainloop()

starter()
