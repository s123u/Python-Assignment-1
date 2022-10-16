
from tkinter import Button, Checkbutton, IntVar, Label, Tk


root=Tk()
root.geometry("500x500")
w=Label(root,text='gujarat university',font="50").pack()


checkbutton1=IntVar()
checkbutton2=IntVar()
checkbutton3=IntVar()
def submit():
    ch1=checkbutton1.get()
    ch2=checkbutton2.get()
    ch3=checkbutton3.get()

    print("tutorial"+ch1)
    print("student"+ch2)
    print("courses"+ch3)
    
    Label(root,text=ch1).pack(padx=20)
    Label(root,text=ch2).pack(padx=20)
    Label(root,text=ch3).pack(padx=20)
    checkbutton1.set("")
    checkbutton2.set("")
    checkbutton3.set("")

button1=Checkbutton(root,text="tutorial",variable=checkbutton1,onvalue=1,offvalue=0,height=2,width=10)
button2=Checkbutton(root,text="student",variable=checkbutton2,onvalue=1,offvalue=0,height=2,width=10)
button3=Checkbutton(root,text="courses",variable=checkbutton3,onvalue=1,offvalue=0,height=2,width=10)

# button1=Checkbutton(root,text="tutorial",variable=checkbutton1,onvalue=1,offvalue=0,height=2,width=10)
# button2=Checkbutton(root,text="student",variable=checkbutton2,onvalue=0,offvalue=1,height=2,width=10)
# button3=Checkbutton(root,text="courses",variable=checkbutton3,onvalue=0,offvalue=0,height=2,width=10)



button1.pack()
button2.pack()
button3.pack()

sub_btn=Button(root,text='Submit',command=submit).pack(padx=20,pady=20)


root.mainloop()