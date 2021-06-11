from tkinter import *

window = Tk()
window.title("計算機")
window.geometry("500x500+100+100")
window.rowconfigure(0, weight = 1) #高
window.columnconfigure(0, weight = 1) #寬
window.rowconfigure(1, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.columnconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1) #高
window.columnconfigure(3, weight = 1) #寬
window.rowconfigure(4, weight = 1)
window.columnconfigure(4, weight = 1)
window.rowconfigure(5, weight = 1)
window.columnconfigure(5, weight = 1)

op = 0
v1 = 0
opFlag = False

def changeText(num):
    if int(lab["text"]) !=0 and opFlag == False:
        lab["text"] = ["text"] + num
    else:
        lab["text"] = num

def opSet(opValue):
    global op
    global v1
    v1 = int(lab['text'])
    op = opValue

def compute():
    v2 = int(lab['text'])
    global op
    if op == 1:
        lab['text'] = v1 + v2
    if op == 2:
        lab['text'] = v1 - v2
    if op == 3:
        lab['text'] = v1 * v2
    if op == 4:
        lab['text'] = v1 / v2

lab = Label(window,text= "0",
                    justify="right",
                    anchor="c",
                    font=("Monaco",26,"bold"),
                    background="#ccddff",
                    foreground="#000000")
lab.grid(row=0, column=0 , columnspan=3, sticky=EW)

But1= Button(window, text="7" , font=("Monaco",30,"bold"), command=lambda:changeText("7"))
But1.grid(row= 1 , column= 0 , sticky=NSEW)
But2= Button(window, text="8", font=("Monaco",30,"bold"), command=lambda:changeText("8"))
But2.grid(row= 1 , column= 1 , sticky=NSEW)
But3= Button(window, text="9", font=("Monaco",30,"bold"), command=lambda:changeText("9"))
But3.grid(row= 1 , column= 2 , sticky=NSEW)
But13= Button(window, text="+" , font=("Monaco",30,"bold"), command=lambda:opSet(1))
But13.grid(row= 1 , column= 3 , sticky=NSEW)

But4= Button(window, text="4" , font=("Monaco",30,"bold"), command=lambda:changeText("4"))
But4.grid(row= 2 , column= 0 , sticky=NSEW)
But5= Button(window, text="5", font=("Monaco",30,"bold"), command=lambda:changeText("5"))
But5.grid(row= 2 , column= 1 , sticky=NSEW)
But6= Button(window, text="6", font=("Monaco",30,"bold"), command=lambda:changeText("6"))
But6.grid(row= 2 , column= 2 , sticky=NSEW)
But10= Button(window, text="-" , font=("Monaco",30,"bold"), command=lambda:opSet(2))
But10.grid(row= 2, column= 3 , sticky=NSEW)

But7= Button(window, text="1" , font=("Monaco",30,"bold"), command=lambda:changeText("1"))
But7.grid(row= 3 , column= 0 , sticky=NSEW)
But8= Button(window, text="2", font=("Monaco",30,"bold"), command=lambda:changeText("2"))
But8.grid(row= 3 , column= 1 , sticky=NSEW)
But9= Button(window, text="3", font=("Monaco",30,"bold") , command=lambda:changeText("3"))
But9.grid(row= 3 , column= 2 , sticky=NSEW)
But10= Button(window, text="*" , font=("Monaco",30,"bold"), command=lambda:opSet(3))
But10.grid(row= 3 , column= 3 , sticky=NSEW)

But10= Button(window, text="=" , font=("Monaco",30,"bold"), command=lambda:compute())
But10.grid(row= 4 , column= 0 , sticky=NSEW)
But11= Button(window, text="0", font=("Monaco",30,"bold"), command=lambda:changeText("0"))
But11.grid(row= 4 , column= 1 , sticky=NSEW)
But12= Button(window, text=".", font=("Monaco",30,"bold"), command=lambda:changeText("."))
But12.grid(row= 4 , column= 2 , sticky=NSEW)
But10= Button(window, text="/" , font=("Monaco",30,"bold"), command=lambda:opSet(4))
But10.grid(row= 4 , column= 3 , sticky=NSEW)

window.mainloop()