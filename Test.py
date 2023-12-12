import tkinter as tk

# Create a temporary Tkinter root window to get screen resolution
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()  # Destroy the temporary window

# Print the screen resolution
print(f"Screen resolution: {screen_width}x{screen_height}")
