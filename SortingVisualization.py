import time
import random
import tkinter as tk
from prueba import bubble_sort, selection_sort, insertion_sort, cocktail_sort, shell_sort
from tkinter import messagebox as mBox
from tkinter import ttk, Canvas, Scale, PhotoImage, Image


class Window:
	def __init__(self, window):
		self.window = window
		self.random_list = []
		self.color = "black"
		self.items_id = []
		self.comp_value = 0
		self.dark_image = PhotoImage(file = "/home/ederivc/Documents/Python/dark_mode.png")
		self.dark_image = self.dark_image.zoom(1)
		self.dark_image = self.dark_image.subsample(30)
		self.canvas = Canvas(self.window, bg = "#f0ffff")
		self.canvas.place(relx = 0, relwidth =1, relheight = 0.80)
		self.display_options()


	def display_options(self):
		lower_frame = tk.Frame(self.window, bg = "#1b3945")
		lower_frame.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)

		algorithm_label = tk.Label(lower_frame, text = "Algorithm", width = 20)
		algorithm_label.place(x = 40, y = 20)

		combo_algorithm = ttk.Combobox(lower_frame,
		                            values=[
		                                    "Bubble sort",
		                                    "Selection sort",
											"Insertion sort",
											"Cocktail shaker sort",
											"Shell sort",
											"Merge sort"],
											font = (8))
		combo_algorithm.place(x = 40, y = 60)
		combo_algorithm.config(font = ("Helvetica"), width = 16)
		combo_algorithm.current(0)

		min_value = tk.Label(lower_frame, text = "Min. Value", width = 20)
		min_value.place(x = 240, y = 20)

		min_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		min_value_number.place(x = 260, y = 60)

		max_value = tk.Label(lower_frame, text = "Max. Value", width = 20)
		max_value.place(x = 440, y = 20)

		max_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		max_value_number.place(x = 460, y = 60)

		speed = tk.Label(lower_frame, text = "Speed", width = 19)
		speed.place(x = 640, y = 20)

		speed_var = tk.Scale(lower_frame, from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
		speed_var.place(x = 660, y = 60)

		new_info_btn = tk.Button(lower_frame, text = "Generate graph", activebackground = "#468499",
		width = 12, command = lambda: self.generate_info(min_value_number.get(), max_value_number.get(), 
		combo_algorithm.get()))
		new_info_btn.place(x = 825, y = 15)

		sort_items = tk.Button(lower_frame, text = "Sort",activebackground = "#468499", width = 12,
		command = lambda: self.select_algorithm(speed_var.get(), combo_algorithm.get()))
		sort_items.place(x = 825, y = 53)

		delete_btn = tk.Button(lower_frame, text = "Delete all",activebackground = "#468499", width = 12,
		command = self.delete_all)
		delete_btn.place(x = 825, y = 90)

		img_label = tk.Label(lower_frame, background = "white", image = self.dark_image)
		img_label.place(x = 950, y = 45)
		img_label.bind('<Button-1>', lambda x: self.dark_screen(lower_frame))


	def comparisons_info(self, comp_value):
		self.canvas.create_text(20,500,anchor = "sw", text = "Comparisons", fill = self.color)
		self.canvas.create_text(130, 500,anchor = "sw", text = comp_value, fill = self.color)


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


	def dark_screen(self, lower_frame):
		if self.color == "black":
			self.canvas.config(bg = "#666666")
			lower_frame.config(bg = "#333333")
			self.canvas.update_idletasks()
			self.color = "white"
		else:
			self.canvas.config(bg = "#f0ffff")
			lower_frame.config(bg = "#1b3945")
			self.canvas.update_idletasks()
			self.color = "black"


	def select_algorithm(self, speed, option):
		if option == "Bubble sort":
			bubble_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Selection sort":
			selection_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Insertion sort":
			insertion_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Cocktail shaker sort":
			cocktail_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Shell sort":
			shell_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Merge sort":
			self.merge_sort(self.random_list , self.speed_values(speed))


	def final_animation(self, comp_value):
		for x in range(len(self.random_list)):
			time.sleep(0.03)
			self.draw_info(comp_value, ["#ff7f50" if i <= x else "#4ca3dd" if i == x+1 else "#badd99" for i in range(len(self.random_list))])
			#self.draw_info(["#f3d3a5" if i <= x else "#4e2c7f" if i == x+1 else "#badd99" fothemer i in range(len(self.random_list))])


	def delete_all(self):
		self.canvas.delete("all")


	def generate_info(self, min_value, max_value, algorithm):
		"""if algorithm == "Merge sort":
			self.generate_small_info(min_value, max_value)
			return"""

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

		return self.draw_info(0, ["#ffa500" for i in range(len(self.random_list))])


	def draw_info(self, comp_value, color):
		self.canvas.delete("all")
		self.comparisons_info(comp_value)
		x = 20
		y = 50
		for key, value in enumerate(self.random_list):
			self.canvas.create_rectangle(x, value[1], y, 10,fill= color[key])
			self.canvas.create_text(x,value[1]+20,anchor = "sw", text = value[0], fill = self.color)
			x += 40
			y += 40

		self.window.update_idletasks()


	def generate_small_info(self, min_value, max_value):
		self.items_id.clear()
		self.comp_value = 0
		self.comparisons_info()
		self.canvas.delete("all")
		if min_value > max_value:
			mBox.showerror("ERROR", "Value error")
			return

		self.canvas.delete("all")
		self.random_list.clear()

		for _ in range(8):
			number = random.randint(min_value, max_value)
			self.random_list.append(number)
		
		return self.draw_small_info(["#ffa500" for i in range(len(self.random_list))])


	def draw_small_info(self, color):
		self.canvas.delete("all")
		self.comparisons_info()
		x = 300
		y = 10
		for value in self.random_list: #x0, y0, x1, y1

			id_item = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="blue")
			id_text = self.canvas.create_text(x+18,50,anchor = "sw", text = value, fill = "black")
			self.items_id.append((value, id_item, id_text))

			x += 50

		self.window.update_idletasks()



	def small_animation(self, arr, ident):
		if len(arr) >= 1 and ident == "L":
			for key, value in enumerate(arr):
				if len(arr) == 4:
					self.canvas.move(value[1], -50, 30)
					self.canvas.move(value[2], -50, 30)

				elif len(arr) == 2:
					self.canvas.move(value[1], -25, 30)
					self.canvas.move(value[2], -25, 30)

				self.canvas.move(value[1], -5, 30)
				self.canvas.move(value[2], -5, 30)

			self.window.update_idletasks()
			time.sleep(0.4)

		if len(arr) >= 1 and ident == "R":
			for key, value in enumerate(arr):
				if len(arr) == 4:
					self.canvas.move(value[1], 50, 30)
					self.canvas.move(value[2], 50, 30)

				elif len(arr) == 2:
					self.canvas.move(value[1], 25, 30)
					self.canvas.move(value[2], 25, 30)

				self.canvas.move(value[1], 5, 30)
				self.canvas.move(value[2], 5, 30)

			self.window.update_idletasks()
			time.sleep(0.4)


	def merge_sort(self, arr, speed):
		if len(arr) <= 1:
			return arr

		mid = int(len(arr) / 2)
		left = arr[:mid]
		right = arr[mid:]
		self.merge_sort(left, speed)
		self.merge_sort(right, speed)
			
		#self.draw_info(self.color_array(len(arr), left, mid, right))
		#time.sleep(0.3)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			arr[k] = left[i]
			i+= 1
			k+= 1

		while j < len(right): 
			arr[k] = right[j]
			j+= 1
			k+= 1

		print(arr)



	"""def merge_sort(self, arr):
		if len(arr) > 1: 
			mid = len(arr)//2 
			L = arr[:mid] # Dividing the array elements  
			R = arr[mid:] # into 2 halves 

			
			self.small_animation(L, "L")
			self.small_animation(R, "R")

			self.merge_sort(L)
			self.merge_sort(R) 
			
		
			i = j = k = 0
				
			while i < len(L) and j < len(R): 
				if L[i] < R[j]:
					for key, value in enumerate(L):
						for key2, value2 in enumerate(R):
							self.canvas.move(value[1], -5, -30) 
							self.canvas.move(value[2], -5, -30) 
							self.canvas.move(value2[1], -10, -30) 
							self.canvas.move(value2[2], -10, -30) 
							break
						break
					self.window.update_idletasks()	
					arr[k] = L[i] 
					i+= 1
				else: 
					for key, value in enumerate(R):
						for key2, value2 in enumerate(L):
							self.canvas.move(value[1], -10, -30) 
							self.canvas.move(value[2], -10, -30) 
							self.canvas.move(value2[1], -5, -30) 
							self.canvas.move(value2[2], -5, -30) 
							break
						break
					self.window.update_idletasks()
					arr[k] = R[j] 
					j+= 1
				k+= 1
				
			
			while i < len(L): 
				for key, value in enumerate(L):
						self.canvas.move(value[1], 50, 5) 
						self.canvas.move(value[2], 50, 5) 
						break
				self.window.update_idletasks()
				arr[k] = L[i] 
				i+= 1
				k+= 1
				
			while j < len(R): 
				for key, value in enumerate(R):
						self.canvas.move(value[1], -50, 5) 
						self.canvas.move(value[2], -50, 5) 
						break
				self.window.update_idletasks()
				arr[k] = R[j] 
				j+= 1
				k+= 1

			for key, value in enumerate(L):
				self.canvas.move(value[1], -50, 30)
				self.canvas.move(value[2], -50, 30)

			self.window.update_idletasks()
			time.sleep(0.4)
			

		print(arr)"""


	"""def bubble_sort(self, speed):
		cont = 1
		for _ in range(len(self.random_list)-1):
			for j in range(len(self.random_list)-1):
				if self.random_list[j] > self.random_list[j+1]:
					temp = self.random_list[j]
					self.random_list[j] = self.random_list[j+1]
					self.random_list[j+1] = temp
					self.comp_value += 1
					time.sleep(speed)
					self.draw_info(["#a0bbe8" if x == j else "#ec7788" if x == j+1 else "#6897bb" if x > len(self.random_list) - cont
					else "#ffa500" for x in range(len(self.random_list))])

			cont += 1

		self.final_animation()"""



if __name__ == "__main__":
	window = tk.Tk()

	width = 1000
	height = 650
	window.minsize(width, height)
	window.title("Algorithm visualization")

	app = Window(window)

	window.mainloop()




