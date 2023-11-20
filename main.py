from tkinter import *
from tkinter import messagebox
from charactersfile import letters, numbers, symbols
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Generate a random password with a random length between 6 and 12 characters
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    # Create a list to store characters for the password
    password_list = []

    # Append random letters, numbers, and symbols to the list
    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    # Shuffle the list to randomize the characters
    random.shuffle(password_list)

    # Concatenate the characters to form the final password
    password = "".join(password_list)

    # Set the generated password to the Entry widget
    password_entry_var.set(password)

    # Using pyperclip to copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_entries():
    # Validate that all entry fields are filled
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if not website_text or not email_text or not password_text:
        # Show an error message if any field is empty
        messagebox.showerror("Error", "All fields are required.")
        return False

    return True


def save():
    if validate_entries():
        # Get the values from the entry fields
        website_text = website_entry.get()
        email_text = email_entry.get()
        password_text = password_entry.get()

        # Ask for confirmation before saving
        result = messagebox.askyesno("Confirmation", "Are you sure you want to proceed?")
        if result:
            # Save the data to a file and clear the entry fields
            with open("data.txt", "a") as file:
                file.write(f"{website_text} | {email_text} | {password_text}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

            # Show a success message
            messagebox.showinfo("Saved!", "Entries saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=50, width=200, height=200)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Variable
password_entry_var = StringVar()

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.insert(0, "charlescollins476@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33, textvariable=password_entry_var)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", highlightthickness=0, command=password_generator)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()
