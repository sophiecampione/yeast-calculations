from tkinter import *
import tkinter
from tkinter import messagebox
import math

# creates window
master = tkinter.Tk()

# creates options for drop down menu & sets default option
OPTIONS = [
    "starting concentration", "final concentration", "duration", "doubling time", "dilution",
]  # etc
var = StringVar(master)
var.set(OPTIONS[0])

# defines labels and unit labels for entry boxes for different selections from drop down menu
labels_sc = ['final concentration: ', 'duration: ', 'doubling time: ']
labels_dil = ['desired concentration: ', 'current concentration: ', 'final volume: ']
labels_dt = ['starting concentration: ', 'duration: ', 'final concentration: ']
labels_dur = ['starting concentration: ', 'final concentration: ', 'doubling time: ']
labels_fc = ['starting concentration: ', 'duration: ', 'doubling time: ']

units_sc = ['cells/mL', 'hours', 'minutes']
units_dil = ['cells/mL', 'cells/mL', 'mL']
units_dt = ['cells/mL', 'hours', 'cells/mL']
units_dur = ['cells/mL', 'cells/mL', 'minutes']
units_fc = ['cells/mL', 'hours', 'minutes']


# defines calculate button
# different calculations for different selections from the drop down menu
def calculate_ok():
    choice = var.get()
    if choice == 'starting concentration':
        try:
            # gets entries
            fin_conc = float(entry.get())
            hours = entry1.get()
            minutes = entry1dur.get()
            dur = float(hours) * 60 + float(minutes)
            dou_time = float(entry2.get())
            # makes sure entries are valid
            assert fin_conc > 0
            assert dur > 0
            assert dou_time > 0
            ##calculates and updates result labels
            value = fin_conc / (2 ** (dur / dou_time))
            value = str(str(value) + " cells/mL")
            result1.config(text="The starting concentration is: ")
            result2.config(text=value)
            # adds dilution entry boxes, button and labels
            de1.grid(row=9, column=1)
            de2.grid(row=10, column=1)
            dil.grid(row=8)
            d1.grid(row=9, column=0)
            d2.grid(row=10, column=0)
            du1.grid(row=9, column=2)
            du2.grid(row=10, column=2)
            button_sc_dil.grid(row=11)
            result3.grid(row=15, column=0)
            result4.grid(row=15, column=1)

            # dilution calculator to dilute from the current concentration to desired starting concentration
            def calc_dil():
                try:

                    start_conc = fin_conc / (2 ** (dur / dou_time))
                    curr_conc = float(de1.get())
                    assert curr_conc > 0
                    assert curr_conc > start_conc
                    fin_vol = float(de2.get())
                    assert fin_vol > 0
                    dilution = start_conc * fin_vol / curr_conc
                    dilution = str(str(dilution) + " mL in " + str(fin_vol) + " mL final volume")
                    result3.config(text="The dilution is: ")
                    result4.config(text=dilution)
                except:
                    messagebox.showerror("Error",
                                         "Please enter values correctly as specified. Make sure current concentration is larger than starting concentration. ")

            button_sc_dil.config(command=calc_dil)


        except:
            messagebox.showerror("Error", "Please enter values correctly as specified.")
    elif choice == 'final concentration':
        try:
            # gets entries, makes sure they're valid, calculates and displays result
            start_conc = float(entry.get())
            hours = entry1.get()
            minutes = entry1dur.get()
            dur = float(hours) * 60 + float(minutes)
            dou_time = float(entry2.get())
            assert start_conc > 0
            assert dur > 0
            assert dou_time > 0
            value = start_conc * 2 ** (dur / dou_time)
            value = str(str(value) + " cells/mL")
            result1.config(text="The final concentration is: ")
            result2.config(text=value)
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified.")
    elif choice == "duration":
        try:
            # gets entries, makes sure they're valid, calculates and displays result
            start_conc = float(entry.get())
            fin_conc = float(entry1.get())
            dou_time = float(entry2.get())
            assert start_conc > 0
            assert fin_conc > 0
            assert dou_time > 0
            assert start_conc < fin_conc
            value = dou_time * math.log(fin_conc / start_conc) / math.log(2)
            hours = int(value / 60)
            minutes = round(value % 60)
            value = str(str(hours) + " hours " + str(minutes) + " mins")

            result1.config(text="The duration is: ")
            result2.config(text=value)
        except:
            messagebox.showerror("Error",
                                 "Please enter values correctly as specified. Make sure starting concentration is less than final concentration.")
    elif choice == "doubling time":
        try:
            # gets entries, makes sure they're valid, calculates and displays result
            start_conc = float(entry.get())
            fin_conc = float(entry2.get())
            hours = entry1.get()
            minutes = entry1dur.get()
            dur = float(hours) * 60 + float(minutes)
            assert start_conc > 0
            assert fin_conc > 0
            assert dur > 0
            assert start_conc < fin_conc
            value = dur * math.log(2) / (math.log(fin_conc / start_conc))
            value = str(str(value) + " minutes ")

            result1.config(text="The doubling time is: ")
            result2.config(text=value)
        except:
            messagebox.showerror("Error",
                                 "Please enter values correctly as specified. Make sure starting concentration is less than final concentration.")
    elif choice == "dilution":
        try:
            # gets entries, makes sure they're valid, calculates and displays result
            des_conc = float(entry.get())
            curr_conc = float(entry1.get())
            fin_vol = float(entry2.get())
            assert des_conc > 0
            assert curr_conc > 0
            assert fin_vol > 0
            assert des_conc < curr_conc
            value = fin_vol * des_conc / curr_conc
            value = str(str(value) + " mL into " + str(fin_vol) + " mL final volume ")

            result1.config(text="The dilution is: ")
            result2.config(text=value)
        except:
            messagebox.showerror("Error",
                                 "Please enter values correctly as specified. Make sure desired concentration is less than current concentration.")


# function to remove the dilution widgets because we only want them visible for sc calculation
def remove_dil():
    d1.grid_remove()
    d2.grid_remove()
    dil.grid_remove()
    de1.grid_remove()
    de2.grid_remove()
    result3.grid_remove()
    result4.grid_remove()
    button_sc_dil.grid_remove()
    du1.grid_remove()
    du2.grid_remove()


# updates text when option is selected to the labels, units defined above
# removes unwanted widgets & places them back
def update_label(value):
    choice = var.get()
    if choice == 'starting concentration':
        labels = labels_sc
        unit = units_sc
        remove_dil()
        entry1dur.grid(row=4, column=3)
        units1dur.grid(row=4, column=4)
    elif choice == 'dilution':
        labels = labels_dil
        unit = units_dil
        remove_dil()
        entry1dur.grid_forget()
        units1dur.grid_forget()
    elif choice == 'duration':
        labels = labels_dur
        unit = units_dur
        remove_dil()
        entry1dur.grid_forget()
        units1dur.grid_forget()
    elif choice == 'final concentration':
        labels = labels_fc
        unit = units_fc
        remove_dil()
        entry1dur.grid(row=4, column=3)
        units1dur.grid(row=4, column=4)
    else:
        labels = labels_dt
        unit = units_dt
        remove_dil()
        entry1dur.grid(row=4, column=3)
        units1dur.grid(row=4, column=4)

    display.config(text=labels[0])
    display1.config(text=labels[1])
    display2.config(text=labels[2])

    units.config(text=unit[0])
    units1.config(text=unit[1])
    units2.config(text=unit[2])

    result1.config(text="")
    result2.config(text="")

    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry1dur.delete(0, 'end')


# creates button
ok_calc_button = Button(master, text="OK", command=calculate_ok).grid(row=6)

# creates the drop down menu
p = tkinter.OptionMenu(master, var, *OPTIONS, command=update_label)
p.grid(row=2)

# creates title
# title = tkinter.Label(master, text = "Yeast Calculator", font = ("Helvetica", 12))
# title.grid(row = 0)

# sets up widgets for entire program, which will be either visible or hidden depending on the options selected
question = tkinter.Label(master, text="Please select calculation below:", font=("Helvetica", 10))
question.grid(row=1)

display = tkinter.Label(master, text=labels_sc[0])
display.grid(row=3, column=0)

entry = tkinter.Entry(master)
entry.grid(row=3, column=1)

units = tkinter.Label(master, text=units_sc[0])
units.grid(row=3, column=2)

display1 = tkinter.Label(master, text=labels_sc[1])
display1.grid(row=4, column=0)

entry1 = tkinter.Entry(master)
entry1.grid(row=4, column=1)
entry1dur = tkinter.Entry(master)
entry1dur.grid(row=4, column=3)

units1 = tkinter.Label(master, text=units_sc[1])
units1.grid(row=4, column=2)
units1dur = tkinter.Label(master, text="minutes")
units1dur.grid(row=4, column=4)

display2 = tkinter.Label(master, text=labels_sc[2])
display2.grid(row=5, column=0)

entry2 = tkinter.Entry(master)
entry2.grid(row=5, column=1)

units2 = tkinter.Label(master, text=units_sc[2])
units2.grid(row=5, column=2)

result1 = tkinter.Label(master)
result1.grid(row=7, column=0)
result2 = tkinter.Label(master)
result2.grid(row=7, column=1)

dil = Label(master, text="Dilution:", font=('Helvetica', 10))
dil.grid(row=8)

d1 = Label(master, text="current concentration:")
d1.grid(row=9, column=0)

d2 = Label(master, text="final volume:")
d2.grid(row=10, column=0)

de1 = Entry(master)
de2 = Entry(master)

du1 = Label(master, text="cells/mL")
du2 = Label(master, text='mL')

button_sc_dil = Button(master, text="Calculate")
button_sc_dil.grid(row=11)

result3 = tkinter.Label(master)
result3.grid(row=15, column=0)

result4 = tkinter.Label(master)
result4.grid(row=15, column=1)

remove_dil()

master.mainloop()