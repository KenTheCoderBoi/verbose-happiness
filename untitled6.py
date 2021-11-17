from tkinter import *
import random

root=Tk()
root.title("jendikjnc")
root.geometry("400x400")

enter = Entry(root)
enter.place(relx=0.5,rely=0.2,anchor=CENTER)
enter2 = Entry(root)
enter2.place(relx=0.5,rely=0.25,anchor=CENTER)
label1 = Label(root)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
label4 = Label(root)
label4.place(relx=0.5,rely=0.45,anchor=CENTER)
label2 = Label(root)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)
label5 = Label(root)
label5.place(relx=0.5,rely=0.65,anchor=CENTER)
label3 = Label(root)
label3.place(relx=0.5,rely=0.65,anchor=CENTER)
list2 = []
list1 = []
def addfriendcommand():
    country = enter.get()
    city = enter2.get()
    list1.append(country)
    list2.append(city)
    label1["text"] = list1
    label4["text"] = list2
def randomcountry():
    length = len(list1)
    randomnum= random.randint(0,length-1)
    label2["text"] = list1[randomnum]
    label3["text"] = list2[randomnum]
    
addfriend = Button(root,text="add country", command=addfriendcommand,anchor=CENTER)
addfriend.place(relx=0.4,rely=0.3)
randomint = Button(root,text="random country", command=randomcountry,anchor=CENTER)
randomint.place(relx=0.4,rely=0.7)

root.mainloop()