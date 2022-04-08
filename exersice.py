'Решение на задача тип Линейно преобразуване на Уолш-Адамар'

import BPA                 #--> Бързо преобразуване
                
import zonal_criterium     #--> Зонален признак
import subdiscretisation   #--> Субдискретизация
import magnitude_criterium #--> Амплитуден признак
import coefficients        #--> За коефициентите
from coefficients          import coefficient_e 

#--------------------------------------------------------------#

# Условие: Да се изчисли трансформантата y' за входния вектор x' при m=8 чрез БПА. 
         # Да се извърши кодиране на трансформантата у' по амплитуден признак, зонален признак (D=3) и субдискретизация.
         # Да се определи коеф. свиване при неравномерна скала и нормираната средноквадратична грешка за трите метода на кодиране.
        

x = [] # --> входен вектор

# Добавяме елементите във входния вектор 
print('Въведете стойността на входния вектор Х')
for i in range(8):    
    element = int(input())
    x.append(element) 

# Изчисляваме първата итерация
y_first_iteration = BPA.first_iteration(x)
print('Първа итерация')
print(y_first_iteration) #--> Трансформантата в първа итерация

# Изчисляваме втората итерация 
y_second_iteration = BPA.second_iteration(y_first_iteration)
print('Втора итерация')
print(y_second_iteration)

# Изчисляваме третата итерация 
y_third_iteration = BPA.third_iteration(y_second_iteration)
print('Трета итерация')
print(y_third_iteration)

# Преобразуваме У
y = BPA.re_order(y_third_iteration)
print('Трансформанта У:')
print(y)

#-----------------Вариации-----------------#
"По амлитуден признак"
  #--Open_Me--
    #y_amplitude = magnitude_criterium.coding_by_magnitude(y)
    #print('Y1:')
    #print(y_amplitude) 
    #
    ## Отново пренареждаме, но този път наобратно
    #y_amplitude = BPA.back_re_order(y_amplitude)
    #print('Пренаредена трансформанта:')
    #print(y_amplitude)
    #
    #x_new = magnitude_criterium.results_from_magnitude_criterium(y_amplitude)

"По зонален признак"
#  _OPEN_ME#
    #y_zonal = zonal_criterium.coding_by_zone(y)
    #print('Y1:')
    #print(y_zonal) 
    ## Отново пренареждаме, но този път наобратно
    #y_zonal = BPA.back_re_order(y_zonal)
    #print('Пренаредена трансформанта:')
    #print(y_zonal)
    #x_new = zonal_criterium.results_from_zonal_criterium(y_zonal)

"По субдискретизация"
 #--OPEN--
    #print()
    #y_subdiscretisated = subdiscretisation.subdiscretisation(y)
    #print('Кодирана трансформанта по субдискретизация:')
    #print(y_subdiscretisated)
    #print('Възстановяваме чрез интерлокация:')
    #y_interlocated = subdiscretisation.interlocation(y_subdiscretisated)
    #print(y_interlocated)
    #y_interlocated=BPA.back_re_order(y_interlocated)
    #print('Пренаредена трансформанта:')
    #print(y_interlocated)
    #x_new = zonal_criterium.results_from_zonal_criterium(y_interlocated)
#-----------------Коефициенти------------#
    #--OPEN
        #e = coefficients.coefficient_e(x, x_new)
        #print('Коефициент епсилон:')
        #print(e*100)
        #
        #Qi, Qa, K = coefficients.k_coefficient(y_interlocated, e)
        #print('Коефициент Qi, Qa, K:')
        #print(f"Qi = {Qi}")
        #print(f"Qa = {Qa}")
        #print(f"K  = {K}")
