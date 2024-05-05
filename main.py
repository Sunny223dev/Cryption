import tkinter as tk

# Create the window
window = tk.Tk()

# Set the title of the window
window.title("Cryption")

# Size of the window
window.geometry("1000x500")

icon_path = r'C:\Users\sunny\OneDrive\Desktop\Cryption\Assets\cryption---logo.ico'
icon = tk.PhotoImage(file=icon_path)

# Set the window icon
window.iconphoto(True, icon) 

# Sidebar
sidebar_frame = tk.Frame(window, bg="#37474f", width=100)
sidebar_frame.pack(side="left", fill="y")

# Bakcground color
window.configure(background='#263238')

# Content that will be shown in the window
label = tk.Label(window, text="hm no")
label.pack()

window.mainloop()
