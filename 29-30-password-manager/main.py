from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, f"{password}")
    pyperclip.copy(f'{password}')

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = (website_entry.get()).title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", message="No Data File Found")
    else:
        if website in data:
            email = (data[website]['email'])
            password = (data[website]['password'])
            messagebox.showinfo(website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror("Error", message=f"No details for {website} website exist.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = (website_entry.get()).title()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showerror("Error", message="You must complete all fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="white")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", fg="white")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky='ew')
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew')

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")
generate_password_button = Button(text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
