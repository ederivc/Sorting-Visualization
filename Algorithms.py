import time


def bubble_sort(speed, random_list, comp_value, draw_info, final_animation):
    cont = 1
    for _ in range(len(random_list)-1):
        for j in range(len(random_list)-1):
            if random_list[j] > random_list[j+1]:
                random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
                comp_value += 1
                time.sleep(speed)
                draw_info(comp_value, ["#a0bbe8" if x == j else "#ec7788" if x == j+1 else "#6897bb" if x > len(random_list) - cont
                                       else "#ffa500" for x in range(len(random_list))])

        cont += 1

    final_animation(comp_value)


def selection_sort(speed, random_list, comp_value, draw_info, final_animation):
    for i in range(len(random_list)):
        min_idx = i
        for j in range(i+1, len(random_list)):
            comp_value += 1
            time.sleep(speed)
            draw_info(comp_value, ["#99badd" if x == min_idx else "#ec7788" if x ==
                      j else "#badd99" if x < i else "#ffa500" for x in range(len(random_list))])
            if random_list[min_idx] > random_list[j]:
                min_idx = j

        random_list[i], random_list[min_idx] = random_list[min_idx], random_list[i]

    final_animation(comp_value)


def insertion_sort(speed, random_list, comp_value, draw_info, final_animation):
	actual = 1
	while actual < len(random_list):
		before = actual
		while before > 0 and random_list[before-1] > random_list[before]:
			comp_value += 1
			time.sleep(speed)
			draw_info(comp_value, ["#99badd" if x == before else "#772a3d" if x == before-1 else "#ec7788" if x == actual else "#badd99"
			if x < actual else "#ffa500" for x in range(len(random_list))])
			random_list[before], random_list[before-1] = random_list[before-1], random_list[before]
			before -= 1
		actual += 1

	final_animation(comp_value)


def cocktail_sort(speed, random_list, comp_value, draw_info, final_animation):
	cont = 0
	temp = 1
	left = 1
	right = len(random_list) - 1
	verif = True
	while verif == True:
		verif = False
		for i in range(right):
			if random_list[i] > random_list[i+1]:
				comp_value += 1
				random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
				time.sleep(speed)
				draw_info(comp_value, ["#99badd" if x == i else "#772a3d" if x == i+1 else "#ec7788" if x > len(random_list) - temp 
				or x < cont else "#ffa500" for x in range(len(random_list))])
				verif = True

		verif = False
		temp += 1

		for i in range(right, left, -1):
			if random_list[i] < random_list[i-1]:
				comp_value += 1
				random_list[i], random_list[i-1] = random_list[i-1], random_list[i]
				time.sleep(speed)
				draw_info(comp_value, ["#99badd" if x == i else "#772a3d" if x == i-1 else "#ec7788" if x > len(random_list) - temp
				or x < cont else "#ffa500" for x in range(len(random_list))])
				verif = True

		if verif == False:
			break

		left += 1
		cont += 1

	final_animation(comp_value)


def shell_sort(speed, random_list, comp_value, draw_info, final_animation):
	div = len(random_list) // 2
	while div > 0:
		for i in range(div, len(random_list)):
			actual = random_list[i]

			comparison = i
			while comparison >= div and random_list[comparison - div] > actual:
				time.sleep(speed)
				draw_info(comp_value, ["#99badd" if x == comparison - div else "#772a3d" if x == comparison else
				"#ffa500" for x in range(len(random_list))])
				random_list[comparison], random_list[comparison - div] =  random_list[comparison - div], random_list[comparison]
				comparison -= div
				comp_value += 1

		div = div // 2

	final_animation(comp_value)
