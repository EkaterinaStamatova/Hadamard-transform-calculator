'Функции за изчисление на К и епсилон'
import numpy as np
import math
n = 8
m = 8

def k_coefficient(y_amplitude,e):
    Qi = 0 #bits
    Qa = 0 #bits
    K  = 0 
    for i in range(len(y_amplitude)):
        if(y_amplitude[i]==0):
            Qi+=1
        else:
            element=0
            if(y_amplitude[i]<0):
                element = math.log(((y_amplitude[i]*y_amplitude[i])+1)/e)
                element = math.ceil(element)
            else:
                element = math.log(((y_amplitude[i]*y_amplitude[i])+1)/e)
                element = math.ceil(element)
            Qa += element*0.5
    
    K = (n*np.log2(m))/(Qi+Qa)
            
    return Qi,Qa,K

def coefficient_e(x_old,x_new):
    difference = []
    sum_numenator = 0
    sum_denominator = 0 
    e = 0

    for i in range(len(x_old)):
        sum_denominator += x_new[i]*x_new[i]
        if(x_old[i]!=x_new[i]):
            value = x_old[i] - x_new[i]
            difference.append(value)
    
    for j in range(len(difference)):
        sum_numenator += difference[j]*difference[j]

    numenator = 0
    denominator = sum_denominator

    for i in range(len(difference)):
        numenator+=difference[i]*difference[i]      

    e = numenator/denominator

    return e