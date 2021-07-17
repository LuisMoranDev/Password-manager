from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(web, email_address, pw):
    if len(web) == 0 or len(email_address) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"For the website: {web}\nThese are the details entered: \n Email: {email_address}\n" f"Password: {pw} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web} | {email_address} | {pw}\n")
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Website Label
website = Label(text="Website:", font=("Arial", 15))
website.grid(column=0, row=1)

#Website Entry
web_entry = Entry()
web_entry.config(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

#Email/Username Label
email = Label(text="Email/Username:", font=("Arial", 15))
email.grid(column=0, row=2)

#Email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

#Password
password = Label(text="Password:", font=("Arial", 15))
password.grid(column=0, row=3)

#Password Entry
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

#Generate Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add", width=35, command=lambda: save_password(web_entry.get(), email_entry.get(), password_entry.get()))
add_button.grid(column=1, row=4, columnspan=2)












window.mainloop()