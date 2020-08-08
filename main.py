import tkinter as tk
from GUI import Window

if __name__ == "__main__":
    window = tk.Tk()

    width = 1000
    height = 650
    window.minsize(width, height)
    window.title("Algorithm visualization")

    app = Window(window)

    window.mainloop()
