from tkinter import * 


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=20)
window.config(padx=20, pady=20)


def calculate():
    """Convert input value to km"""
    miles = input.get()
    km = int(miles) * 1.609
    label3.config(text=format(km, '.2f'))
    

# entry box
input = Entry(width=5)
input.grid(row=0, column=1)
input.get()

# miles, km, is equal, label (3)
label1 = Label(text="Miles", font=('Times New Roman', 20, 'normal'))
label1.grid(row=0, column=2)
label1.config(padx=5, pady=5)

label2 = Label(text="Km", font=('Times New Roman', 20, 'normal'))
label2.grid(row=1, column=2)
label2.config(padx=5, pady=5)



# km value label 
label3 = Label(text=0, font=('Times New Roman', 20, 'normal'))
label3.grid(row=1, column=1)
label3.config(padx=5, pady=5)

# label that displays conversion 
# calculate button

button = Button(text='Calculate', command=calculate)
button.grid(row=2, column=1)

window.mainloop()