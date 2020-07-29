import time
import random
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import ttk, Canvas, Scale


class Window:
	def __init__(self, window):
		self.window = window
		self.random_list = []
		self.comp_value = 0
		self.canvas = Canvas(self.window, bg = "#f0ffff")
		self.canvas.place(relx = 0, relwidth =1, relheight = 0.80)
		self.display_options()


	def display_options(self):
		lower_frame = tk.Frame(self.window, bg = "#675d50")
		lower_frame.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)

		algorithm_label = tk.Label(lower_frame, text = "Algorithm", width = 20)
		algorithm_label.place(x = 40, y = 20)

		combo_algorithm = ttk.Combobox(lower_frame,
		                            values=[
		                                    "Bubble sort",
		                                    "Selection sort",
											"Insertion sort"],
											font = (8))
		combo_algorithm.place(x = 40, y = 60)
		combo_algorithm.config(font = ("Helvetica"), width = 16)
		combo_algorithm.current(0)

		min_value = tk.Label(lower_frame, text = "Min. Value", width = 20)
		min_value.place(x = 240, y = 20)

		min_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		min_value_number.place(x = 270, y = 60)

		max_value = tk.Label(lower_frame, text = "Max. Value", width = 20)
		max_value.place(x = 440, y = 20)

		max_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		max_value_number.place(x = 470, y = 60)

		new_info_btn = tk.Button(lower_frame, text = "Generate graph", activebackground = "#678f71",
		width = 12, command = lambda: self.generate_info(min_value_number.get(), max_value_number.get()))
		new_info_btn.place(x = 825, y = 15)

		speed = tk.Label(lower_frame, text = "Speed", width = 19)
		speed.place(x = 640, y = 20)

		speed_var = tk.Scale(lower_frame, from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
		speed_var.place(x = 670, y = 60)

		sort_items = tk.Button(lower_frame, text = "Sort",activebackground = "#678f71", width = 12,
		command = lambda: self.select_algorithm(speed_var.get(), combo_algorithm.get()))
		sort_items.place(x = 825, y = 53)

		delete_btn = tk.Button(lower_frame, text = "Delete all",activebackground = "#678f71", width = 12,
		command = self.delete_all)
		delete_btn.place(x = 825, y = 90)


	def comparisons_info(self):
		self.canvas.create_text(20,500,anchor = "sw", text = "Comparisons", fill = "black")
		self.canvas.create_text(130, 500,anchor = "sw", text = self.comp_value, fill = "black")


	def speed_values(self, speed):
		if speed == 1:
			return 0.4
		elif speed == 2:
			return 0.3
		elif speed == 3:
			return 0.2
		elif speed == 4:
			return 0.1
		else:
			return 0.08


	def select_algorithm(self, speed, option):
		if option == "Bubble sort":
			self.bubble_sort(self.speed_values(speed))

		elif option == "Selection sort":
			self.selection_sort(self.speed_values(speed))

		elif option == "Insertion sort":
			self.insertion_sort(self.speed_values(speed))


	def final_animation(self):
		for x in range(len(self.random_list)):
			time.sleep(0.03)
			self.draw_info(["#f3d3a5" if i <= x else "#4e2c7f" if i == x+1 else "#badd99" for i in range(len(self.random_list))])


	def delete_all(self):
		self.canvas.delete("all")


	def generate_info(self, min_value, max_value):
		self.comp_value = 0
		self.comparisons_info()
		self.canvas.delete("all")
		if min_value > max_value:
			mBox.showerror("ERROR", "Value error")
			return

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

		return self.draw_info(["#cc5c5c" for i in range(len(self.random_list))])


	def draw_info(self, color):
		self.canvas.delete("all")
		self.comparisons_info()
		x = 20
		y = 50
		for key, value in enumerate(self.random_list):
			self.canvas.create_rectangle(x, value[1], y, 10,fill= color[key])
			self.canvas.create_text(x,value[1]+20,anchor = "sw", text = value[0], fill = "black")
			x += 40
			y += 40

		self.window.update_idletasks()


	def bubble_sort(self, speed):
		for _ in range(len(self.random_list)-1):
			for j in range(len(self.random_list)-1):
				if self.random_list[j] > self.random_list[j+1]:
					temp = self.random_list[j]
					self.random_list[j] = self.random_list[j+1]
					self.random_list[j+1] = temp
					self.comp_value += 1
					time.sleep(speed)
					self.draw_info(["#a0bbe8" if x == j else "#74b741" if x == j+1 else "#cc5c5c" for x in range(len(self.random_list))])

		#self.draw_info(["#badd99" for i in range(len(self.random_list))])
		self.final_animation()


	def selection_sort(self, speed):
		for i in range(len(self.random_list)):
			min_idx = i
			for j in range(i+1, len(self.random_list)):
				self.comp_value += 1
				time.sleep(speed)
				self.draw_info(["#99badd" if x == min_idx else "#fee11a" if x == j else "#badd99" if x < i else "#cc5c5c" for x in range(len(self.random_list))])
				if self.random_list[min_idx] > self.random_list[j]:
					min_idx = j

			self.random_list[i], self.random_list[min_idx] = self.random_list[min_idx], self.random_list[i]

		#self.draw_info(["#badd99" for i in range(len(self.random_list))])
		self.final_animation()


	def insertion_sort(self, speed):
		actual = 1
		while actual < len(self.random_list):
			before = actual
			while before > 0 and self.random_list[before-1] > self.random_list[before]:
				self.comp_value += 1
				time.sleep(speed)
				self.draw_info(["#99badd" if x == before or x == before-1 else "#fee11a" if x == actual else "#badd99"
				if x < actual else "#cc5c5c" for x in range(len(self.random_list))])
				self.random_list[before], self.random_list[before-1] = self.random_list[before-1], self.random_list[before]
				before -= 1
			actual += 1

		#self.draw_info(["#badd99" for i in range(len(self.random_list))])
		self.final_animation()


if __name__ == "__main__":
	window = tk.Tk()

	width = 1000
	height = 650
	window.minsize(width, height)
	window.title("Algorithm visualization")

	app = Window(window)

	window.mainloop()
