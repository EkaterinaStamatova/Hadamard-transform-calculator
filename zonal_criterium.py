"Кодиране по зонален признак"

import math
import BPA
# Дефинираме константата С
d = 3

def coding_by_zone(y):
    
    for i in range(len(y)):
        if(i>d):
            y[i]=0 
        elif(i<=d):
            continue
    
    return y

def divide_by_eight(y):
     for i in range(len(y)):
        y[i]=math.ceil(y[i]/8 )     
     return y

def results_from_zonal_criterium(y_amplitude):
    # Намираме новия Х
        x_first_iteration = BPA.first_iteration(y_amplitude)
        print("Първа итерация:")
        print(x_first_iteration)
        x_second_iteration = BPA.second_iteration(x_first_iteration)
        print("Втора итерация:")
        print(x_second_iteration)
        x_third_iteration = BPA.third_iteration(x_second_iteration)
        print("Трета итерация:")
        print(x_third_iteration)

        x_new = divide_by_eight(x_third_iteration)
        print("Нова стойност на Х")
        print(x_new)

        return x_new