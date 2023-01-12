from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)


is_equal_label = Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=5, pady=5)

conversion = Label(text="0", font=("Arial", 16, "bold"))
conversion.grid(column=1, row=1)
conversion.config(padx=5, pady=5)

km_label = Label(text="km", font=("Arial", 18, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)


def button_pressed():
    user_input = float(miles_input.get())
    kilometers = round(user_input * 1.60934, 2)
    conversion.config(text=f"{kilometers}")


button = Button(text="Calculate", command=button_pressed)
button.grid(column=1, row=3)
button.config(padx=1, pady=1)


window.mainloop()
