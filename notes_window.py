# Needed imports
from tkinter import Tk, Label

# If none will open if not wont open another window
notes_window = None

def open_notes_window():
    global notes_window
    
    # Create the notes window if it hasn't been created yet
    if notes_window is None:
        notes_window = Tk()
        notes_window.title("Cryption - Notes")
        notes_label = Label(notes_window, text="")
        notes_label.pack(padx=20, pady=10)
        
        # Set window size
        window_width = 700
        window_height = 400
        window_geometry = "%dx%d" % (window_width, window_height)
        notes_window.geometry(window_geometry)
        
        # Center window
        screen_width = notes_window.winfo_screenwidth()
        screen_height = notes_window.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        notes_window.geometry("+%d+%d" % (x_coordinate, y_coordinate))
        
        # Background color
        notes_window.configure(background='#263238')
        
        # Reset notes_window var when closed
        notes_window.protocol("WM_DELETE_WINDOW", on_notes_window_close)
        
        # Make window not resizable
        notes_window.resizable(False, False)
        
        # It do be loopin
        notes_window.mainloop()

# Reset the global variable when the window is closed
def on_notes_window_close():
    global notes_window
    notes_window.destroy()
    notes_window = None
