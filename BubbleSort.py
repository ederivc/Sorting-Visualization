import time

def bubble_sort(my_list, draw):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                time.sleep(0.2)
                draw(my_list, ['black' if x == j or x == j+1 else 'white' for x in range(len(my_list))])

    draw(my_list, ["black" for x in range(len(my_list))])            
