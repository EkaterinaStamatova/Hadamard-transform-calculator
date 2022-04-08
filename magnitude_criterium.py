"Кодиране по амплитуден признак"
import math
import BPA
# Дефинираме константата С
c = [10 ,5 ,3.33, 2.5, 2, 1.67, 1.43, 1.25]

def coding_by_magnitude(y):
    
    for i in range(len(y)):
        if(abs(y[i])>c[i]):
            continue
        elif(abs(y[i])<c[i]):
            y[i]=0 
    
    return y

def divide_by_eight(y):
     for i in range(len(y)):
        y[i]=math.ceil(y[i]/8 )     
     return y

def results_from_magnitude_criterium(y_amplitude):
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