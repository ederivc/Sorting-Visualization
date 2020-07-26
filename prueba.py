import time
import random
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import ttk, Canvas
from BubbleSort import bubble_sort

window = tk.Tk()

width = 1100
height = 755
window.maxsize(width, height)
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

canvas = Canvas(window, bg="blue")
canvas.place(relx = 0, relwidth =1, relheight = 0.69)

def generate_numbers(min_value, max_value):
    while True:
        if min_value >= max_value:
            mBox.showerror("Error", "Error")
            return 0

        random_list = []

        for i in range(0, 27):
            number = random.randint(min_value, max_value)
            random_list.append(number)

        return random_list


def draw_data(sorted_list):
    if sorted_list == 0:
        pass

    canvas.delete("all")
    posx = 20
    posy = 50
    max_value = max(sorted_list)

    global values_list
    values_list = []
    for i in sorted_list:
        height_value = int(i * 500 / max_value)

        if height_value <= 9:
            values_list.append((i, 9))
            continue

        values_list.append((i, height_value))

    print(values_list)

    for key, values in values_list:
        canvas.create_rectangle(posx, values, posy, 10, fill = "white")
        canvas.create_text(posx+10,values+19,anchor = "sw", text=key, fill ="white")
        posx += 40
        posy += 40

    window.update_idletasks()


def draw(sorted_list, color):
    canvas.delete("all")
    posx = 20
    posy = 50

    for key, values in enumerate(sorted_list):
        canvas.create_rectangle(posx, values[1], posy, 10, fill = color[key])
        canvas.create_text(posx+10,values[1]+19,anchor = "sw", text=values[0], fill ="white")
        posx += 40
        posy += 40

    window.update_idletasks()


lower_frame = tk.Frame(window, bg = "red")
lower_frame.place(relx = 0, rely = 0.70, relwidth = 1, relheight = 1)


sorted_name = tk.Label(lower_frame, text = "Algorithm", bg = "blue", font=("Helvetica", 20))
sorted_name.place(x = 40, y = 20)


combo_algorithm = ttk.Combobox(lower_frame,
                            values=[
                                    "Bubble sort",
                                    "February",
                                    "March",
                                    "April"])
combo_algorithm.place(x = 10, y = 60)
combo_algorithm.config(font = ("Helvetica", 15))
combo_algorithm.current(0)

min_value = tk.Label(lower_frame, text = "Min. Value", bg = "blue", font=("Helvetica", 20))
min_value.place(x = 470, y = 20)

min_value_number = tk.StringVar()
min_value_entry = tk.Entry(lower_frame, width = 17, textvariable = min_value_number)
min_value_entry.place(x = 470, y = 60)

max_value = tk.Label(lower_frame, text = "Max. Value", bg = "blue", font=("Helvetica", 20))
max_value.place(x = 900, y = 20)

max_value_number = tk.StringVar()
max_value_entry = tk.Entry(lower_frame, width = 17, textvariable = max_value_number )
max_value_entry.place(x = 900, y = 60)

sumbmit_button = tk.Button(lower_frame, text = "Generate", width = 15,
command = lambda: draw_data(generate_numbers(int(min_value_number.get()), int(max_value_number.get()))))
sumbmit_button.place(x = 10, y = 100)

sort_button = tk.Button(lower_frame, text = "Visualize", width = 15, command = lambda: bubble_sort(values_list,
draw))
sort_button.place(x = 465, y = 120)

window.mainloop()
