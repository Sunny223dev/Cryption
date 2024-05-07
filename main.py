# Needed imports for code to work
import tkinter as tk

# Create the window
window = tk.Tk()

# Set the title of the window
window.title("Cryption - Password Manager")

# Size of the window
window.geometry("1200x650")

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

# Background color
window.configure(background='#263238')

# Content that will be shown in the window
label = tk.Label(window, text="hm no")
label.pack()

# It do be loopin
window.mainloop()
