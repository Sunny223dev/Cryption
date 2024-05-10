# Needed imports
from tkinter import Tk, Label

# If none will open if not wont open another window
profile_window = None

def open_profile_window():
    global profile_window
    
    # Create the profile window if it hasnt been yet
    if profile_window is None:
        profile_window = Tk()
        profile_window.title("Cryption - Account")
        profile_label = Label(profile_window, text="")
        profile_label.pack(padx=20, pady=10)
        
        # Set window size
        window_width = 700
        window_height = 400
        window_geometry = "%dx%d" % (window_width, window_height)
        profile_window.geometry(window_geometry)
        
        # Center window
        screen_width = profile_window.winfo_screenwidth()
        screen_height = profile_window.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        profile_window.geometry("+%d+%d" % (x_coordinate, y_coordinate))
        
        # Background color
        profile_window.configure(background='#263238')
        
        # Reset profile_window var when closed
        profile_window.protocol("WM_DELETE_WINDOW", on_profile_window_close)
        
        # Make window not resizable
        profile_window.resizable(False, False)
        
        # It do be loopin
        profile_window.mainloop()

# Reset the global variable when the window is closed
def on_profile_window_close():
    global profile_window
    profile_window.destroy()
    profile_window = None
