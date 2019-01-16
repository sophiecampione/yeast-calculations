from tkinter import *
import tkinter
from tkinter import messagebox
import math

#creates window
master =tkinter.Tk()


#creates options for drop down menu & sets default option
OPTIONS = [
"starting concentration (cells/mL)", "final concentration(cells/mL)",  "duration (hr, min)", "doubling time (min)", "dilution",
] #etc
var = StringVar(master)
var.set(OPTIONS[0])



# defines labels for entry boxes for different selections from drop down menu
labels_sc = ['final concentration (cells/mL)', 'duration (please enter as HH MM)', 'doubling time (min)']
labels_dil = ['desired concentration (cells/mL)', 'current concentration (cells/mL)','final volume (mL)' ]
labels_dt = ['starting concentration (cells/mL)', 'final concentration (cells/mL)', 'duration (please enter as HH MM)']
labels_dur = ['starting concentration (cells/mL)', 'final concentration (cells/mL)', 'doubling time (min)']
labels_fc = ['starting concentration (cells/mL)', 'duration (please enter as HH MM)', 'doubling time (min)']





# defines calculate button
# different calculations for different selections from the drop down menu
def calculate_ok():
    choice = var.get()
    if choice == 'starting concentration (cells/mL)':
        try:
            fin_conc = float(entry.get())
            dur = entry1.get()
            dur = dur.split( )
            dur = float(dur[0])*60 + float(dur[1])
            dou_time = float(entry2.get())
            assert fin_conc>0
            assert dur>0
            assert dou_time>0
            value = fin_conc/(2**(dur/dou_time))
            value = str(str(value) + " cells/mL")
            result1.config(text = "The starting concentration is: ")
            result2.config(text = value)
            
            btn = Button (master, text ="Dilution")
            btn.grid(row = 8)
            
            def dilution():
                start_conc = fin_conc/(2**(dur/dou_time))
                d1 = Label(master, text = "current concentration:")
                d1.grid(row = 9, column = 0)
                d2 = Label(master, text = "final volume")
                d2.grid(row = 10, column = 0)
                de1 = Entry(master)
                de1.grid(row =  9, column = 1)
                de2 = Entry (master)
                de2.grid(row = 10, column = 1)
                button = Button (master, text = "Calculate")
                button.grid(row = 11)
                btn.grid_forget()
                def dil_calc():
                    curr_conc = float(de1.get())
                    assert curr_conc >0
                    fin_vol = float(de2.get())
                    assert fin_vol>0
                    dilution = start_conc * fin_vol/curr_conc
                    dilution = str(str(dilution)+" mL in " +str(fin_vol)+" mL final volume")
                    result1.config (text = "The dilution is: ")
                    result2.config(text = dilution)
                    d1.destroy()
                    d2.destroy()
                    de1.destroy()
                    de2.destroy()
                    button.grid_forget()
                button.config(command = dil_calc)
                
            btn.config(command = dilution)
            
            
            
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified.")
    elif choice == 'final concentration(cells/mL)':
        try:
            start_conc = float(entry.get())
            dur = entry1.get()
            dur = dur.split( )
            dur = float(dur[0])*60 + float(dur[1])
            dou_time = float(entry2.get())
            assert start_conc>0
            assert dur>0
            assert dou_time>0
            value = start_conc*2**(dur/dou_time)
            value = str(str(value) + " cells/mL")
            
            result1.config(text = "The final concentration is: ")
            result2.config(text = value)
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified.")
    elif choice == "duration (hr, min)":
        try:
            start_conc = float(entry.get())
            fin_conc = float(entry1.get())
            dou_time = float(entry2.get())
            assert start_conc>0
            assert fin_conc>0
            assert dou_time>0
            assert start_conc<fin_conc
            value = dou_time * math.log(fin_conc/start_conc)/math.log(2)
            hours = int(value / 60)
            minutes = round(value % 60)
            value = str(str(hours)+ " hours " + str(minutes)+" mins") 
                   
            result1.config(text = "The duration is: ")
            result2.config(text = value)
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified. Make sure starting concentration is less than final concentration.")
    elif choice == "doubling time (min)":
        try:
            start_conc = float(entry.get())
            fin_conc = float(entry1.get())
            dur = entry2.get()
            dur = dur.split( )
            dur = float(dur[0])*60 + float(dur[1])
            assert start_conc>0
            assert fin_conc>0
            assert dur>0
            assert start_conc < fin_conc
            value = dur * math.log(2)/(math.log(fin_conc/start_conc))
            value = str(str(value)+ " minutes ") 
                   
            result1.config(text = "The doubling time is: ")
            result2.config(text = value)
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified. Make sure starting concentration is less than final concentration.")
    elif choice == "dilution":
        try:
            des_conc = float(entry.get())
            curr_conc = float(entry1.get())
            fin_vol = float(entry2.get())
            assert des_conc>0
            assert curr_conc>0
            assert fin_vol>0
            assert des_conc < curr_conc
            value = fin_vol * des_conc / curr_conc
            value = str(str(value)+ " mL into " +str(fin_vol)+" mL final volume ") 
                   
            result1.config(text = "The dilution is: ")
            result2.config(text = value)
        except:
            messagebox.showerror("Error", "Please enter values correctly as specified. Make sure desired concentration is less than current concentration.")
        

    
            


#updates text when option is selected to the labels defined above
def update_label(value):
    choice = var.get()
    if choice == 'starting concentration (cells/mL)':
        labels = labels_sc
    elif choice == 'dilution':
        labels = labels_dil
    elif choice == 'duration (hr, min)':
        labels = labels_dur
    elif choice == 'final concentration(cells/mL)':
        labels = labels_fc
    else:
        labels = labels_dt
    
    display.config(text = labels[0])
    display1.config(text = labels[1])
    display2.config(text = labels[2])
    result1.config(text = "")
    result2.config(text = "")
    
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    
ok_calc_button = Button(master, text="OK", command=calculate_ok).grid(row=6)
    
    

#creates the drop down menu
p = tkinter.OptionMenu(master, var, *OPTIONS, command=update_label)
p.grid(row = 2)

#sets up entry boxes and labels
question = tkinter.Label(master, text = "Please select calculation below:", font=("Helvetica", 10))
question.grid(row = 1)

display = tkinter.Label(master, text = labels_sc[0])
display.grid(row = 3, column = 0)

entry = tkinter.Entry(master)
entry.grid(row = 3, column = 1)

display1 = tkinter.Label(master, text = labels_sc[1])
display1.grid(row = 4, column = 0)

entry1 = tkinter.Entry(master)
entry1.grid(row = 4, column = 1)

display2 = tkinter.Label(master, text = labels_sc[2])
display2.grid(row = 5, column = 0)

entry2 = tkinter.Entry(master)
entry2.grid(row = 5, column = 1)

result1 = tkinter.Label(master)
result1.grid(row = 15, column = 0)
result2 = tkinter.Label(master)
result2.grid(row = 15, column =1)



master.mainloop()