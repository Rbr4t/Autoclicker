# Autoclicker program written in Python programming language
import pyautogui, tkinter, threading, keyboard, os
from time import sleep
master = tkinter.Tk()
master.title("AUTOCLICKER")
master.config(bg="#6fd189")

width = 350
height = 400
master.geometry(f"{width}x{height}")
master.resizable(False, False)

#stuff I got from internet and this is what should make .exe file functional
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

master.iconbitmap(resource_path2('cursorico.ico'))

#function which creates a new thread and starts clicking where the cursor is.
def clicking(clicks, interval, clickTime, button, x_cord=None, y_cord=None):
    global stop_thread
    
        
    time_to = {"s": 1, "min": 60, "h": 360}
    sleep(2)
    
    while not stop_thread and threading.main_thread().is_alive():
        def stop():
            global stop_thread
            stop_thread = True
            switch()
            
        keyboard.add_hotkey('f6', lambda: stop())
        
        if clickTime == "ms":
            try: pyautogui.click(x=x_cord, y=y_cord, clicks=clicks, interval=interval/60, button=button)
            except: pyautogui.click(clicks=clicks, interval=interval/60, button=button)
        else:
            try: pyautogui.click(x=x_cord, y=y_cord, clicks=clicks, interval=interval*time_to[clickTime], button=button)
            except: pyautogui.click(clicks=clicks, interval=interval*time_to[clickTime], button=button)
        
    
stop_thread = False

#fuction which changes Start to Stop sign on the main button.
def switch():
    global stop_thread
    global is_on
    global interval #secs between clicks
    global current_mousebutton
    global var #clicks in row
    global clickTime #in what units time is measured
    global x_axis, y_axis
    global static
    if static.get()=="choose":
        try: start_clicking = threading.Thread(target=clicking, args=(int(var.get()), int(interval.get()), clickTime.get(), current_mousebutton.get(), int(x_axis.get()), int(y_axis.get())))
        except: start_clicking = threading.Thread(target=clicking, args=(int(var.get()), int(interval.get()), clickTime.get(), current_mousebutton, int(x_axis.get()), int(y_axis.get())))
    else:
        try: start_clicking = threading.Thread(target=clicking, args=(int(var.get()), int(interval.get()), clickTime.get(), current_mousebutton.get()))
        except: start_clicking = threading.Thread(target=clicking, args=(int(var.get()), int(interval.get()), clickTime.get(), current_mousebutton))
    
    if is_on:
        button.config(text="STOP autoclicker (F6)") 
        is_on = False
        stop_thread = False
        
        
        start_clicking.start()
        
    else:
        button.config(text="START autoclicker (F6)")
        is_on = True
        stop_thread = True
        

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
frame_clickInt = tkinter.Frame(master, height=60)
frame_clickInt.place(x= 160, y=150)
labelInt = tkinter.Label(frame_clickInt, text="Interval between clicks", font=("Times New Roman", 10))

default_interval_value = tkinter.IntVar(None, 60)
default_interval_measure = tkinter.StringVar(None, "ms")
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

static = tkinter.StringVar(None, "current") #where to click

def unresponsive():
    global x_axis
    global y_axis
    static.set("current")
    x_axis.config(state="disabled")
    y_axis.config(state="disabled")

def responsive():
    global x_axis
    global y_axis
    static.set("choose")
    x_axis.config(state="normal")
    y_axis.config(state="normal")

radioCurrent = tkinter.Radiobutton(frame_cursor, text="Current position", value="current", variable=static, command=lambda: unresponsive())
radioChoose = tkinter.Radiobutton(frame_cursor, text="Choose position", value="choose", variable=static, command= lambda: responsive())

labelCur.pack(anchor="w", padx=10)
radioCurrent.pack(side="left")
radioChoose.pack(side="left")

#entry for cordinates which to click
frame_cursor_Entry = tkinter.Frame(master)
frame_cursor_Entry.place(x=150, y=350)

validation2 = frame_cursor_Entry.register(only_numbers)

lableX = tkinter.Label(frame_cursor_Entry, text="X")
x_axis = tkinter.Entry(frame_cursor_Entry, bd=4, width=5, validate="key", validatecommand=(validation2, '%S'), state="disabled")

lableY = tkinter.Label(frame_cursor_Entry, text="Y")
y_axis = tkinter.Entry(frame_cursor_Entry, bd=4, width=6, validate="key", validatecommand=(validation2, '%S'), state="disabled")

lableX.pack(side="left")
x_axis.pack(side="left")
lableY.pack(side="left")
y_axis.pack(side="left")

#mainloop method
master.mainloop()