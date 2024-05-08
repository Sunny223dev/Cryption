# Needed imports for code to work
import tkinter as tk

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
sidebar_frame = tk.Frame(window, bg="#37474f", width=120)
sidebar_frame.pack(side="left", fill="y")
sidebar_frame.pack_propagate(0)

# Adds profile account icon to the sidebar
profile_account_icon_path = r'Assets\Sidebar - Icons\profile-account-icon.ico'
profile_account_icon = tk.PhotoImage(file=profile_account_icon_path)
profile_account_icon = profile_account_icon.subsample(7)
profile_account_icon_label = tk.Label(sidebar_frame, image=profile_account_icon, bg="#37474f")
profile_account_icon_label.pack(pady=10)

# Adds lock add icon to the sidebar
lock_add_icon_path = r'Assets\Sidebar - Icons\lock-add-icon.ico'
lock_add_icon = tk.PhotoImage(file=lock_add_icon_path)
lock_add_icon = lock_add_icon.subsample(7)
lock_add_icon_label = tk.Label(sidebar_frame, image=lock_add_icon, bg="#37474f")
lock_add_icon_label.pack(pady=10)

# Background color
window.configure(background='#263238')

# Content that will be shown in the window
label = tk.Label(window, text="hm no")
label.pack()

# It do be loopin
window.mainloop()
