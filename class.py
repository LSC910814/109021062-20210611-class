from tkinter import *

flag = True
def setBtnText(num):
    global flag
    if num == 0:
        if flag:
            btn0.config(text="O")
        else:
            btn0.config(text="X")
        btn0.config(state=DISABLED) #按鈕按過後不能使用
    elif num == 1:
        if flag:
            btn1.config(text="O")
        else:
            btn1.config(text="X")
        btn1.config(state=DISABLED)
    elif num == 2:
        if flag:
            btn2.config(text="O")
        else:
            btn2.config(text="X")
        btn2.config(state=DISABLED)
    elif num == 3:
        if flag:
            btn3.config(text="O")
        else:
            btn3.config(text="X")
        btn3.config(state=DISABLED)
    elif num == 4:
        if flag:
            btn4.config(text="O")
        else:
            btn4.config(text="X")
        btn4.config(state=DISABLED)
    elif num == 5:
        if flag:
            btn5.config(text="O")
        else:
            btn5.config(text="X")
        btn5.config(state=DISABLED)
    elif num == 6:
        if flag:
            btn6.config(text="O")
        else:
            btn6.config(text="X")
        btn6.config(state=DISABLED)
    elif num == 7:
        if flag:
            btn7.config(text="O")
        else:
            btn7.config(text="X")
        btn7.config(state=DISABLED)
    elif num == 8:
        if flag:
            btn8.config(text="O")
        else:
            btn8.config(text="X")
        btn8.config(state=DISABLED)
    flag = not flag
    
    if btn0.cget('text') == btn1.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
        if btn0.cget('text') == "X":
            print("P2 is winner")
    if btn3.cget('text') == btn4.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "O":
            print("P1 is winner")
        if btn3.cget('text') == "X":
            print("P2 is winner")
    if btn6.cget('text') == btn7.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "O":
            print("P1 is winner")
        if btn6.cget('text') == "X":
            print("P2 is winner")
    if btn0.cget('text') == btn3.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
        if btn0.cget('text') == "X":
            print("P2 is winner")
    if btn1.cget('text') == btn4.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "O":
            print("P1 is winner")
        if btn1.cget('text') == "X":
            print("P2 is winner")
    if btn3.cget('text') == btn5.cget('text') == btn8.cget('text'):
        if btn3.cget('text') == "O":
            print("P1 is winner")
        if btn3.cget('text') == "X":
            print("P2 is winner")
    if btn0.cget('text') == btn4.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "O":
            print("P1 is winner")
        if btn0.cget('text') == "X":
            print("P2 is winner")
    if btn2.cget('text') == btn4.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "O":
            print("P1 is winner")
        if btn2.cget('text') == "X":
            print("P2 is winner")


window = Tk() #建立空白視窗
window.title("class")
window.geometry("500x500+100+100") #視窗位置
window.rowconfigure(0, weight = 1) #高
window.columnconfigure(0, weight = 1) #寬
window.rowconfigure(1, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.columnconfigure(2, weight = 1)

btn0 = Button(window, text="", command=lambda:setBtnText(0))#lambda函式效果
btn0.grid(row = 0, column = 0, sticky="nsew") 
btn1 = Button(window, text="", command=lambda:setBtnText(1))
btn1.grid(row = 0, column = 1, sticky="nsew")
btn2 = Button(window, text="", command=lambda:setBtnText(2))
btn2.grid(row = 0, column = 2, sticky="nsew")
btn3 = Button(window, text="", command=lambda:setBtnText(3))
btn3.grid(row = 1, column = 0, sticky="nsew")
btn4 = Button(window, text="", command=lambda:setBtnText(4))
btn4.grid(row = 1, column = 1, sticky="nsew")
btn5 = Button(window, text="", command=lambda:setBtnText(5))
btn5.grid(row = 1, column = 2, sticky="nsew")
btn6 = Button(window, text="", command=lambda:setBtnText(6))
btn6.grid(row = 2, column = 0, sticky="nsew")
btn7 = Button(window, text="", command=lambda:setBtnText(7))
btn7.grid(row = 2, column = 1, sticky="nsew")
btn8 = Button(window, text="", command=lambda:setBtnText(8))
btn8.grid(row = 2, column = 2, sticky="nsew")



window.mainloop() #顯示