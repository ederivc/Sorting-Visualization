def bubble_sort(self, speed):
		cont = 1
		for _ in range(len(self.random_list)-1):
			for j in range(len(self.random_list)-1):
				if self.random_list[j] > self.random_list[j+1]:
					temp = self.random_list[j]
					self.random_list[j] = self.random_list[j+1]
					self.random_list[j+1] = temp
					self.comp_value += 1
					time.sleep(speed)
					self.draw_info(["#a0bbe8" if x == j else "#74b741" if x == j+1 else "#6897bb" if x > len(self.random_list) - cont
					else "#ffa500" for x in range(len(self.random_list))])

			cont += 1

		self.final_animation()


def selection_sort(self, speed):
		for i in range(len(self.random_list)):
			min_idx = i
			for j in range(i+1, len(self.random_list)):
				self.comp_value += 1
				time.sleep(speed)
				self.draw_info(["#99badd" if x == min_idx else "#fee11a" if x == j else "#badd99" if x < i else "#ffa500" for x in range(len(self.random_list))])
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
				if x < actual else "#ffa500" for x in range(len(self.random_list))])
				self.random_list[before], self.random_list[before-1] = self.random_list[before-1], self.random_list[before]
				before -= 1
			actual += 1

		#self.draw_info(["#badd99" for i in range(len(self.random_list))])
		self.final_animation()


def cocktail_sort(self):
		cont = 0
		temp = 1
		left = 1
		right = len(self.random_list) - 1
		verif = True
		while verif == True:
			verif = False
			for i in range(right):
				if self.random_list[i] > self.random_list[i+1]:
					self.comp_value += 1
					self.random_list[i], self.random_list[i+1] = self.random_list[i+1], self.random_list[i]
					time.sleep(0.1)
					self.draw_info(["#99badd" if x == i else "#fee11a" if x == i+1 else "#6897bb" if x > len(self.random_list) - temp 
					or x < cont else "#ffa500" for x in range(len(self.random_list))])
					verif = True

			verif = False
			temp += 1

			for i in range(right, left, -1):
				if self.random_list[i] < self.random_list[i-1]:
					self.comp_value += 1
					self.random_list[i], self.random_list[i-1] = self.random_list[i-1], self.random_list[i]
					time.sleep(0.1)
					self.draw_info(["#99badd" if x == i else "#fee11a" if x == i-1 else "#6897bb" if x > len(self.random_list) - temp
					or x < cont else "#ffa500" for x in range(len(self.random_list))])
					verif = True

			if verif == False:
				break

			left += 1
			cont += 1

		self.final_animation()