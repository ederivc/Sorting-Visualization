import sys
import time
import random
import tkinter as tk
from tkinter import ttk, Canvas, Scale


class Window:
	def __init__(self, window):
		self.window = window
		self.random_list = []
		self.canvas = Canvas(self.window, bg = "white")
		self.canvas.place(relx = 0, relwidth =1, relheight = 0.69)
		self.display_options()


	def display_options(self):
		lower_frame = tk.Frame(self.window, bg = "gray")
		lower_frame.place(relx = 0, rely = 0.69, relwidth = 1, relheight = 1)

		algorithm_label = tk.Label(lower_frame, text = "Algorithm", width = 20)
		algorithm_label.place(x = 40, y = 20)

		combo_algorithm = ttk.Combobox(lower_frame,
		                            values=[
		                                    "Bubble sort",
		                                    "Selection sort"], 
											font = (8))
		combo_algorithm.place(x = 40, y = 60)
		combo_algorithm.config(font = ("Helvetica"), width = 16)
		combo_algorithm.current(0)

		min_value = tk.Label(lower_frame, text = "Min. Value", width = 20)
		min_value.place(x = 300, y = 20)

		min_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 10)
		min_value_number.place(x = 300, y = 60)

		max_value = tk.Label(lower_frame, text = "Max. Value", width = 20)
		max_value.place(x = 560, y = 20)

		max_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 10)
		max_value_number.place(x = 560, y = 60)

		new_info_btn = tk.Button(lower_frame, text = "Generate", activebackground = "#678f71",
		command = lambda: self.generate_info(min_value_number.get(), max_value_number.get()))
		new_info_btn.place(x = 820, y = 30)   

		speed = tk.Label(lower_frame, text = "Speed")
		speed.place(x = 400, y = 120)

		speed_var = tk.Scale(lower_frame, from_=1, to=5, orient=tk.HORIZONTAL)
		speed_var.place(x = 450, y = 120)

		sort_items = tk.Button(lower_frame, text = "Sort",activebackground = "#678f71",
		command = lambda: self.select_algorithm(speed_var.get(), combo_algorithm.get()))
		sort_items.place(x = 837, y = 65)


	def select_algorithm(self, speed, option):
		if option == "Bubble sort":
			self.bubble_sort(speed)

		elif option == "Selection sort":
			self.selection_sort(speed)


	def generate_info(self, min_value, max_value):
		self.canvas.delete("all")
		self.random_list.clear()

		for i in range(24):
			number = random.randint(min_value, max_value)
			self.random_list.append(number)

		max_value = max(self.random_list)
		temp_list = []

		for i in self.random_list:				            
			height_value = 	int(i * 450 / max_value)	 #max_value = 450  -> i?

			if height_value <= 9:
				temp_list.append((i, 9))
				continue

			temp_list.append((i, height_value))			 #[(1, 10), (32, 300)]

		self. random_list = temp_list
		print(self.random_list)

		return self.draw_info(["gray" for i in range(len(self.random_list))])


	def draw_info(self, color):
		self.canvas.delete("all")
		x = 20
		y = 50
		for key, value in enumerate(self.random_list):
			self.canvas.create_rectangle(x, value[1], y, 10,fill= color[key])
			self.canvas.create_text(x,value[1]+20,anchor = "sw", text = value[0], fill = "black")
			x += 40
			y += 40

		self.window.update_idletasks()


	def bubble_sort(self, speed_var):
	    for i in range(len(self.random_list)-1):
	        for j in range(len(self.random_list)-1):
	            if self.random_list[j] > self.random_list[j+1]:
	                temp = self.random_list[j]
	                self.random_list[j] = self.random_list[j+1]
	                self.random_list[j+1] = temp
	                time.sleep(speed_var/10)
	                self.draw_info(["black" if x == j or x == j+1 else "gray" for x in range(len(self.random_list))])          

	    self.draw_info(["black" for i in range(len(self.random_list))])


	def selection_sort(self, speed):
		for i in range(len(self.random_list)):
			min_idx = i
			for j in range(i+1, len(self.random_list)):
				if self.random_list[min_idx] > self.random_list[j]:
					temp = self.random_list[min_idx]
					self.random_list[min_idx] = self.random_list[j]
					self.random_list[j] = temp
					time.sleep(speed/10)
					self.draw_info(["black" if x == min_idx or x == j else "gray" for x in range(len(self.random_list))])

		self.draw_info(["black" for i in range(len(self.random_list))])


if __name__ == "__main__":
	window = tk.Tk()

	width = 1000
	height = 700
	window.minsize(width, height)
	window.title("Algorithm visualization")

	app = Window(window)

	window.mainloop()