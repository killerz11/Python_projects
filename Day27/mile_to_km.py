from tkinter import *

def miles_to_km():
    in_km = round(float(input.get()) * 1.609,2)
    label2 = Label(text=f"{in_km}")
    label2.grid(row=1, column=1)

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=100, height=100)
window.config(padx=20,pady=20)

input = Entry(width=10)
input.grid(row=0, column=1)
input.insert(END, string="0")

label = Label(text="Miles")
label.grid(row=0, column=2)

label1 = Label(text="is equal to")
label1.grid(row=1,column=0)

label3 = Label(text="Km")
label3.grid(row=1,column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)






window.mainloop()