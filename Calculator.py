import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("570x550")
root.resizable(False,False)
root.configure(bg="#282C35")

label_result=tk.Label(root,height=4,text="",font=("arial",24),bg="#002147",fg="#FFFFFF")
label_result.pack(fill=tk.X)
label_result.pack()


calculation=""

def show(value):
    global calculation
    calculation+=value
    label_result.config(text=calculation)

def clear():
    global calculation
    calculation=""
    label_result.config(text=calculation)

def calculate():
    global calculation
    calculation = calculation.replace("X", "*")
    result = ""
    if calculation != "":
        try:
            result = str(eval(calculation))
            label_result.config(text=result)
        except:
            result = "Error"
        calculation = result


tk.Button(root,text="7",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("7")).place(x=0,y=150)
tk.Button(root,text="8",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("8")).place(x=140,y=150)
tk.Button(root,text="9",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("9")).place(x=280,y=150)
tk.Button(root,text="/",width=8,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("/")).place(x=420,y=150)


tk.Button(root,text="4",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("4")).place(x=0,y=250)
tk.Button(root,text="5",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("5")).place(x=140,y=250)
tk.Button(root,text="6",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("6")).place(x=280,y=250)
tk.Button(root,text="x",width=8,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("X")).place(x=420,y=250)


tk.Button(root,text="1",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("1")).place(x=0,y=350)
tk.Button(root,text="2",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("2")).place(x=140,y=350)
tk.Button(root,text="3",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("3")).place(x=280,y=350)
tk.Button(root,text="+",width=8,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("+")).place(x=420,y=350)

tk.Button(root,text="0",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("0")).place(x=0,y=450)
tk.Button(root,text="=",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: calculate()).place(x=140,y=450)
tk.Button(root,text="C",width=7,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: clear()).place(x=280,y=450)
tk.Button(root,text="-",width=8,height=2,font=("arial",24,"bold"),bd=1,fg="#fff",bg="#666",command=lambda: show("-")).place(x=420,y=450)


root.mainloop()
