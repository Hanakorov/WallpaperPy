import struct
import ctypes
from tkinter import Tk, Label, Button, filedialog, messagebox


SPI_SETDESKWALLPAPER = 20


def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64


def changeBG(path):
    """Change desktop background depending on bit size"""
    try:
        if is_64bit_windows():
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to change wallpaper:\n{e}")


def select_image():
    """Open file dialog to select an image"""
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        label_selected.config(text=f"Selected: {file_path}", fg="lime")
        changeBG(file_path)


# Create the main Tkinter window
root = Tk()
root.title("Wallpaper Changer")
root.geometry("500x300")
root.resizable(False, False)

# Add a dark theme background color
root.configure(bg="#2b2b2b")

# Add a title label
label_title = Label(
    root, 
    text="Wallpaper Changer", 
    font=("Arial", 18, "bold"), 
    bg="#2b2b2b", 
    fg="white"
)
label_title.pack(pady=20)

# Add an instruction label
label_instruction = Label(
    root, 
    text="Click the button below to select an image:", 
    font=("Arial", 12), 
    bg="#2b2b2b", 
    fg="white"
)
label_instruction.pack(pady=10)

# Add a button to select the image
button_select = Button(
    root, 
    text="Choose Image", 
    command=select_image, 
    font=("Arial", 12), 
    bg="#444444", 
    fg="white", 
    activebackground="#555555", 
    activeforeground="white", 
    padx=20, 
    pady=10, 
    relief="raised", 
    borderwidth=2
)
button_select.pack(pady=10)

# Add a label to display the selected image path
label_selected = Label(
    root, 
    text="No image selected", 
    font=("Arial", 10), 
    bg="#2b2b2b", 
    fg="gray", 
    wraplength=480
)
label_selected.pack(pady=10)

# Run the application
root.mainloop()
