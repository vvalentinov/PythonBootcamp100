import tkinter as tk
from json import JSONDecodeError
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DATA_FILE_NAME = "data.json"

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
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    password = password_entry.get()
    email_username = email_username_entry.get()

    new_data = {
        website: {
            "Email/Username": email_username,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You can't leave any fields empty!")
    else:
        try:
            file = open(DATA_FILE_NAME, "r")
            try:
                data_dictionary = json.load(file)
            except JSONDecodeError:
                data_dictionary = {}
            data_dictionary.update(new_data)
            file = open(DATA_FILE_NAME, "w")
            json.dump(data_dictionary, file, indent=4)  # type: ignore
            file.close()
        except FileNotFoundError:
            new_file = open(DATA_FILE_NAME, "w")
            json.dump(new_data, new_file, indent=4)  # type: ignore
            new_file.close()
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

# ---------------------------- Search Data File ------------------------------- #

def find_password():

    website = website_entry.get().lower()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="You can't leave the website field empty!")
    else:
        try:
            file = open(DATA_FILE_NAME, "r")
            try:
                data_dictionary = dict((k.lower(), v) for k,v in json.load(file).items())
            except JSONDecodeError:
                data_dictionary = {}
            file.close()
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No data file found!")
        else:
            try:
                data = data_dictionary[website]
                messagebox.showinfo(title="Website Found", message=f"Email/Username: {data["Email/Username"]}\nPassword: {data["Password"]}")
            except KeyError:
                messagebox.showinfo(title="Oops", message="No details for the website exists!")

# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# Logo Image
logo_image = tk.PhotoImage(file="logo.png")

# Canvas

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, borderwidth=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = tk.Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_username_entry = tk.Entry(width=35)
email_username_entry.insert(0, "test@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons

generate_pass_btn = tk.Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(column=2, row=3)
add_btn = tk.Button(text="Add", width=30, command=save)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn = tk.Button(text="Search", width=25, command=find_password)
search_btn.grid(column=2, row=1)

root.mainloop()
