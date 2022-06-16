# Autoclicker program written in Python programming language
import pyautogui
import tkinter
import time
import threading

master = tkinter.Tk()
master.title("AUTOCLICKER")
master.config(bg="#45d9b6")

width = 350
height = 400
master.geometry(f"{width}x{height}")
master.resizable(True, False)

#function which creates a new thread and starts clicking where the cursor is.
def clicking(clicks,interval, clickTime, button):
    global stop_thread
    time_to = {"s": 1, "min": 60, "h": 360}
    time.sleep(2)
    while True:
        
        if stop_thread:
            break
        
        if clickTime == "ms":
            pyautogui.click(clicks=clicks, interval=interval/60, button=button)
        else:
            pyautogui.click(clicks=clicks, interval=interval*time_to[clickTime], button=button)
        
stop_thread = False

#fuction which changes Start to Stop sign on the main button.
def switch():
    global stop_thread
    global is_on
    global interval #secs between clicks
    global current_mousebutton
    global var #clicks in row
    global clickTime #in what units time is measured
    
    start_clicking = threading.Thread(target=clicking, args=(int(var.get()), int(interval.get()), clickTime.get(), current_mousebutton.get()))
    
    if is_on:
        button.config(text="STOP autoclicker (F6)") 
        is_on = False
        stop_thread = False
        print("Started autoclicker!")
        start_clicking.start()
        
        
    else:
        button.config(text="START autoclicker (F6)")
        is_on = True
        stop_thread = True
        print("Stopped autoclicker!")

#function for changing mousebutton
def change_mousebutton(button_new):
    global current_mousebutton
    current_mousebutton = button_new
    
def only_numbers(char):
    return char.isdigit()


#variable for text change on main button
is_on = True

#main button
frame = tkinter.Frame(master)
frame.place(x= 10, y=150)

button = tkinter.Button(master, text="START autoclicker (F6)", width=25, height=5, command= lambda: switch())

button.pack(pady=15)

#How many clicks in a row
labelfreq = tkinter.Label(frame, text="Clicking frequancy:", font=("Times New Roman", 10))
var = tkinter.IntVar(None, 1)

radiobutton1 = tkinter.Radiobutton(frame, text="One click", value=1, variable=var)
radiobutton2 = tkinter.Radiobutton(frame, text="Two clicks", value=2, variable=var)
radiobutton3 = tkinter.Radiobutton(frame, text="Three clicks", value=3, variable=var)

labelfreq.pack()
radiobutton1.pack(anchor="w")
radiobutton2.pack(anchor="w")
radiobutton3.pack(anchor="w")

#Interval
frame_clickInt = tkinter.Frame(master)
frame_clickInt.place(x= 160, y=150)
labelInt = tkinter.Label(frame_clickInt, text="Interval between clicks", font=("Times New Roman", 10))

default_interval_value = tkinter.IntVar(None, 60)
default_interval_measure = tkinter.StringVar(None, "ms")
print(default_interval_value.get())
validation1 = frame_clickInt.register(only_numbers)

interval = tkinter.Spinbox(frame_clickInt, from_=1, to=3000, width=8, textvariable=default_interval_value, validate="key", validatecommand=(validation1, '%S'))
clickTime = tkinter.Spinbox(frame_clickInt, values=["ms", 's', 'min', 'h'], width=5, textvariable=default_interval_measure, state='readonly')

labelInt.pack(padx=10)
interval.pack(padx=10, side="left")
clickTime.pack(padx=10, side="left")

#choosing button
frame_button = tkinter.Frame(master)
frame_button.place(x=160, y= 210)
label_button = tkinter.Label(frame_button, text="Choose mousebutton:", font=("Times New Roman", 10))

current_mousebutton = tkinter.StringVar(frame_button, value="left") #currently selected mousebutton, by default its left

frame_button_L = tkinter.Button(frame_button, text="Left", command=lambda : change_mousebutton("left"), activeforeground="red")
frame_button_R = tkinter.Button(frame_button, text="Right", command=lambda : change_mousebutton("right"), activeforeground="red")
frame_button_M = tkinter.Button(frame_button, text="Middle", command=lambda : change_mousebutton("middle"), activeforeground="red")

label_button.pack()
frame_button_L.pack(side="left", padx=7)
frame_button_M.pack(side="left", padx=7)
frame_button_R.pack(side="left", padx=7)

#cursor position
frame_cursor = tkinter.Frame(master)
frame_cursor.place(x=10, y=277)
labelCur = tkinter.Label(frame_cursor, text="Choose your mouse position:", width=38)

var2 = tkinter.StringVar(None, "current") #where to click
def unresponsive():
    global x_axis
    global y_axis
    x_axis.config(state="disabled")
    y_axis.config(state="disabled")

def responsive():
    global x_axis
    global y_axis
    x_axis.config(state="normal")
    y_axis.config(state="normal")

radioCurrent = tkinter.Radiobutton(frame_cursor, text="Current position", value="current", variable=var2, command=lambda: unresponsive())
radioChoose = tkinter.Radiobutton(frame_cursor, text="Choose position", value="choose", variable=var2, command= lambda: responsive())

labelCur.pack(anchor="w", padx=10)
radioCurrent.pack(side="left")
radioChoose.pack(side="left")

#entry for cordinates which to click
frame_cursor_Entry = tkinter.Frame(master)
frame_cursor_Entry.place(x=150, y=350)


validation2 = frame_cursor_Entry.register(only_numbers)


lableX = tkinter.Label(frame_cursor_Entry, text="X")
x_axis = tkinter.Entry(frame_cursor_Entry, bd=4, width=5, validate="key", validatecommand=(validation2, '%S'))
lableY = tkinter.Label(frame_cursor_Entry, text="Y")
y_axis = tkinter.Entry(frame_cursor_Entry, bd=4, width=6, validate="key", validatecommand=(validation2, '%S'))

lableX.pack(side="left")
x_axis.pack(side="left")
lableY.pack(side="left")
y_axis.pack(side="left")

#mainloop method
master.mainloop()