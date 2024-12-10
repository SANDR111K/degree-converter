import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Degree converter")

# The code which opens the window in the middle of the screen.
window_width = 350
window_height = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
#___________________________________________________________________

#There are labels.__________________________________
title_label = tk.Label(root,
                       text= "DEGREE / FAHRENHEIT",
                       font=("Arial", 22),
                       background="MidNightBlue",
                       foreground= "White", 
                       padx = 20,
                       pady = 20,
                       )
title_label.pack()

entry_label = tk.Label(root,
                       text= "NUMBER :",
                       font=("Arial", 12),
                       )
entry_label.place(x=10, y= 100)

from_label = tk.Label(root,
                      text= "FROM :",
                      font=("Arial", 12)
                      )
from_label.place(x=10, y=130)

to_label = tk.Label(root,
                      text= "TO :",
                      font=("Arial", 12)
                      )
to_label.place(x=10, y=160)
#_________________________________________________

#There are enrtyes___________________________________________________________
number_entry = tk.Entry(root, width=23)
number_entry.place(x = 95, y = 103)

from_entry = ttk.Combobox(state="readonly", values=["Celcius", "Fahrenheit"])
from_entry.place(x = 95, y = 133)

to_entry = ttk.Combobox(state="readonly", values=["Celcius", "Fahrenheit"])
to_entry.place(x = 95, y = 163)
#_____________________________________________________________________________

# Label for displaying results or errors__________________
result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.place(x=20, y=230)                            
#_________________________________________________________

def getter():
    number_of = number_entry.get()
    from_degree = from_entry.get()
    to_degree = to_entry.get()
    
    if number_of.isdigit():
        if int(number_of) > 0:
            if from_degree: 
                if to_degree:
                    if from_degree == to_degree:
                        return "Values must be different."
                    elif from_degree != to_degree:
                        return number_of, from_degree, to_degree

def calculator():
    if getter() != "Values must be different.":
        number_of, from_degree, to_degree = getter()
    else: 
        return False
    if from_degree == "Fahrenheit":
        c = (float(number_of) - 32) * 5 / 9
        return c
    elif from_degree == "Celcius":
        f = float(number_of) * (9 / 5) + 32
        return f

def printer():
    # Clear the previous text
    result_label.config(text="")
    
    try:
        result = calculator()
        if getter() != "Values must be different.":
            number_of, from_degree, to_degree = getter()
        else:
            result_label.config(text="Values must be different.")
            return

        # Check if result is a number before formatting
        if isinstance(result, (int, float)):
            result_label.config(text=f"{number_of} {from_degree} INTO {to_degree} = {result:.2f}")
        else:
            result_label.config(text="VALUES MUST BE DIFFERENT.")
    except UnboundLocalError:
        # Do nothing if the error occurs
        pass


button = tk.Button(root, 
                  text= "CALCULATE", 
                  background="MidNightBlue", 
                  foreground="Black",
                  font=("Arial", 10),
                  command=printer
                  )
button.place(x= 120, y = 200)

root.mainloop()
