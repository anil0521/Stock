import tkinter as tk
from tkinter import filedialog
import check_buttons as chk_btn

global IP_Folder
global OP_Folder

def input_folder():
    IP_Folder.set(filedialog.askdirectory())
    #print(folder)

def output_folder():
    OP_Folder.set(filedialog.askdirectory())
    #print(folder)

window = tk.Tk()
IP_Folder = tk.StringVar()
OP_Folder = tk.StringVar()

window.title("Stock Masseuse")
window.geometry("1800x1400")

canvas = tk.Canvas(window, width = 1800, height = 1400)
canvas.pack()
rect = canvas.create_rectangle(30, 190, 600,300)


CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(window, text = "Avg",variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
#C1.pack()
C1.place(x=30,y=170)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(window, text = "Sqrt",variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
#C1.pack()
C2.place(x=150,y=170)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(window, text = "Daily Returns",variable = CheckVar3, onvalue = 1, offvalue = 0, height=5, width = 20)
#C1.pack()
C3.place(x=270,y=170)

CheckVar4 = tk.IntVar()
C4 = tk.Checkbutton(window, text = "Log",variable = CheckVar4, onvalue = 1, offvalue = 0, height=5, width = 20)
#C1.pack()
C4.place(x=410,y=170)



input_label= tk.Label(window,text="Input Folder :").place(x=50,y=60)
tk.Entry(window,textvariable=IP_Folder).place(x = 140, y = 60)
button1 = tk.Button(window,text="Browse",command=input_folder).place(x=280,y=55)

output_label=tk.Label(window,text="Output Folder :").place(x=50,y=90)
tk.Entry(window,textvariable=OP_Folder).place(x = 140, y = 90)
button2 = tk.Button(window,text="Browse",command=output_folder).place(x=280 ,y=85)

#frame_label=tk.Label(window,text="Data Sets:").place(x=60,y=170)


window.mainloop()

