

# Hello, from Kashaf's side.
# I've made a calculator using 'Python'. And i've used tkinter to create an appealing interface.

import tkinter


window=tkinter.Tk()
window.title("K's CALCULATOR")
window.geometry("243x322")


window.config(bg="black")
entry=tkinter.Entry(window,font=("new times roman",18,"bold"),bg="black",fg="white",width=10)
entry.grid(row=1,column=0,columnspan=4,rowspan=5,sticky=("nsew"),padx=8,pady=4)


def on_button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tkinter.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tkinter.END)
            entry.insert(0, 'Error')
    elif value == "C":
        entry.delete(0, tkinter.END)
    else:
        entry.insert(tkinter.END, value)




button1=tkinter.Button(window,text="1",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(1))
button1.grid(column=0, row=6,sticky="s",padx=3,pady=3)
button2=tkinter.Button(window,text="2",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(2))
button2.grid(column=1, row=6,sticky="s",padx=3,pady=3)
button3=tkinter.Button(window,text="3",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(3))
button3.grid(column=2, row=6,sticky="s",padx=3,pady=3)
button4=tkinter.Button(window,text="4",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(4))
button4.grid(column=3,row=6,sticky="s",padx=3,pady=3)

button5=tkinter.Button(window,text="5",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(5))
button5.grid(column=0, row=7,sticky="nsewsew",padx=3,pady=3)
button6=tkinter.Button(window,text="6",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(6))
button6.grid(column=1, row=7,sticky="nsew",padx=3,pady=3)
button7=tkinter.Button(window,text="7",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(7))
button7.grid(column=2, row=7,sticky="nsew",padx=3,pady=3)
button8=tkinter.Button(window,text="8",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(8))
button8.grid(column=3, row=7,sticky="nsew",padx=3,pady=3  )

button9=tkinter.Button(window,text="9",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(9))
button9.grid(column=0, row=8,sticky="nsewsew",padx=3,pady=3)
button10=tkinter.Button(window,text="0",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click(0))
button10.grid(column=1, row=8,sticky="nsew",padx=3,pady=3)
button11=tkinter.Button(window,text=".",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("."))
button11.grid(column=2, row=8,sticky="nsew",padx=3,pady=3)
button12=tkinter.Button(window,text="-",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("-"))
button12.grid(column=3, row=8,sticky="nsew",padx=3,pady=3)

button13=tkinter.Button(window,text="+",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("+"))
button13.grid(column=0, row=9,sticky="nsewsew",padx=3,pady=3)
button14=tkinter.Button(window,text="x",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("*"))
button14.grid(column=1, row=9,sticky="nsew",padx=3,pady=3)
button15=tkinter.Button(window,text="/",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("/"))
button15.grid(column=2, row=9,sticky="nsew",padx=3,pady=3)
button16=tkinter.Button(window,text="=",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("="))
button16.grid(column=3, row=9,sticky="nsew",padx=3,pady=3  )

button17=tkinter.Button(window,text="C",font=("new times roman",11,"bold"),fg="white",bg="dark slate grey",height=2,width=5,command=lambda:on_button_click("C"))
button17.grid(column=0, row=10,columnspan=4,sticky="nsew",padx=3,pady=3  )


window.mainloop()