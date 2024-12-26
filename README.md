# WallpaperPy
 Utility to change desktop wallpaper via path (ctypes, tkinter, struct)
 ##Check if 64 bit
  ```python
  def is_64bit_windows():
    return struct.calcsize('P') * 8 == 64
  ```
## Change desktop background depending on bit size
  ```python
  def changeBG(path):
    try:
        if is_64bit_windows():
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to change wallpaper:\n{e}")
  ```
## Open file dialog to select an image
  ```python
  def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        label_selected.config(text=f"Selected: {file_path}", fg="lime")
        changeBG(file_path)
  ```
