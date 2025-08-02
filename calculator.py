from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                
        scvalue.set(value)
        screen.update()
    
    elif text == "CE":
        scvalue.set("")
        screen.update()
    
    elif text == "c":
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    

root = Tk()
root.geometry("450x600")
root.title("Calculator")
root.wm_iconbitmap("calc_calculator_10824.ico")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 25 bold", bd=25, insertwidth=1, width=25, borderwidth=5)
screen.pack(side=TOP,pady=50, padx=50)

frame = Frame(root, bg="blue")

button = Button(frame, text="%", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="CE", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="c", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="=", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

frame.pack()



frame = Frame(root, bg="blue")

button = Button(frame, text="7", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="8", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="9", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="/", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

frame.pack()


frame = Frame(root, bg="blue")

button = Button(frame, text="4", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="5", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="6", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="*", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

frame.pack()


frame = Frame(root, bg="blue")

button = Button(frame, text="1", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="2", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="3", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="-", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

frame.pack()


frame = Frame(root, bg="blue")

button = Button(frame, text="0", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="00", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text=".", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

button = Button(frame, text="+", padx=5, pady=5, font="lucida 25 bold", bd=5)
button.pack(side=LEFT, padx=2, pady=2)
button.bind("<Button-1>", click)

frame.pack()


root.mainloop()

