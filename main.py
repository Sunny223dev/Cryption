# Needed imports for code to work
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import profile_window
import notes_window
import password_gen_window
import add_password_window

# Open profile window when clicked
def open_profile_window():
    profile_window.open_profile_window()
    
    # Open notes window when clicked
def open_notes_window():
    notes_window.open_notes_window()
    
    # Open password gen window when clicked
def open_password_gen_window():
    password_gen_window.open_password_gen_window()
    
    # Open add password window when clicked
def open_add_password_window():
    add_password_window.open_add_password_window()

# Centers Window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Create the window
window = tk.Tk()

# Set the title of the window
window.title("Cryption - Password Manager")

# Size of the window
window.geometry("1200x650")

# Centers window
center_window(window)

# Make window not resizable
window.resizable(False, False)

# Set icon of window
icon_path = r'Assets\Other - Assets\cryption-logo.ico'
icon = tk.PhotoImage(file=icon_path)
window.iconphoto(True, icon) 

# Sidebar
sidebar_frame = tk.Frame(window, bg="#37474f", width=80)
sidebar_frame.pack(side="left", fill="y")
sidebar_frame.pack_propagate(0)

# Adds profile account icon to the sidebar
profile_account_icon_path = r'Assets\Sidebar - Icons\profile-account-icon.ico'
new_width = 70
new_height = 70
profile_account_img = Image.open(profile_account_icon_path)
profile_account_img = profile_account_img.resize((new_width, new_height), Image.BICUBIC) 
tk_profile_account_img = ImageTk.PhotoImage(profile_account_img)
profile_account_icon_label = Label(sidebar_frame, image=tk_profile_account_img, bg="#37474f")
profile_account_icon_label.pack(pady=5)

# Open profile window when clicked
def open_profile_window():
    profile_window.open_profile_window()

# Create a button using the profile icon image
profile_button = Button(sidebar_frame, image=tk_profile_account_img, bg="#37474f", bd=0, command=open_profile_window, takefocus=False, cursor="hand2", highlightbackground="#37474f", highlightcolor="#37474f")
profile_button.pack(pady=5)

# Adds house icon to the sidebar
house_icon_path = r'Assets\Sidebar - Icons\house-icon.ico'
new_width = 70
new_height = 70
house_img = Image.open(house_icon_path)
house_img = house_img.resize((new_width, new_height), Image.BICUBIC) 
tk_house_img = ImageTk.PhotoImage(house_img)
house_icon_label = Label(sidebar_frame, image=tk_house_img, bg="#37474f")
house_icon_label.pack(pady=5)

# Adds notes icon to the sidebar
notes_icon_path = r'Assets\Sidebar - Icons\notes-icon.ico'
new_width = 96
new_height = 96
notes_img = Image.open(notes_icon_path)
notes_img = notes_img.resize((new_width, new_height), Image.BICUBIC) 
tk_notes_img = ImageTk.PhotoImage(notes_img)
notes_icon_label = Label(sidebar_frame, image=tk_notes_img, bg="#37474f")
notes_icon_label.pack(pady=5)

# Open profile window when clicked
def open_notes_window():
    notes_window.open_notes_window()

# Create a button using the profile icon image
notes_button = Button(sidebar_frame, image=tk_notes_img, bg="#37474f", bd=0, command=open_notes_window, takefocus=False, cursor="hand2", highlightbackground="#37474f", highlightcolor="#37474f")
notes_button.pack(pady=5)

# Adds lock add icon to the sidebar
lock_add_icon_path = r'Assets\Sidebar - Icons\lock-add-icon.ico'
new_width = 60
new_height = 60
lock_add_img = Image.open(lock_add_icon_path)
lock_add_img = lock_add_img.resize((new_width, new_height), Image.BICUBIC) 
tk_lock_add_img = ImageTk.PhotoImage(lock_add_img)
lock_add_icon_label = Label(sidebar_frame, image=tk_lock_add_img, bg="#37474f")
lock_add_icon_label.pack(pady=5)

# Adds key gen icon to the sidebar
key_gen_icon_path = r'Assets\Sidebar - Icons\key-gen-icon.ico'
new_width = 100
new_height = 100
key_gen_img = Image.open(key_gen_icon_path)
key_gen_img = key_gen_img.resize((new_width, new_height), Image.BICUBIC) 
tk_key_gen_img = ImageTk.PhotoImage(key_gen_img)
key_gen_icon_label = Label(sidebar_frame, image=tk_key_gen_img, bg="#37474f")
key_gen_icon_label.pack(pady=5)

# Adds settings icon to the sidebar
settings_icon_path = r'Assets\Sidebar - Icons\settings-icon.ico'
new_width = 100
new_height = 100
settings_img = Image.open(settings_icon_path)
settings_img = settings_img.resize((new_width, new_height), Image.BICUBIC) 
tk_settings_img = ImageTk.PhotoImage(settings_img)
settings_icon_label = Label(sidebar_frame, image=tk_settings_img, bg="#37474f")
settings_icon_label.pack(pady=5)

# Placement of the icons
profile_account_icon_label.place(x=3, y=10)
house_icon_label.place(x=3, y=160)
notes_icon_label.place(x=-8, y=235)
lock_add_icon_label.place(x=8, y=330)
key_gen_icon_label.place(x=-11.8, y=390)
settings_icon_label.place(x=-8, y=553)

# Background color
window.configure(background='#263238')

# Content that will be shown in the window
label = tk.Label(window, text="hm no")
label.pack()

# It do be loopin
window.mainloop()
