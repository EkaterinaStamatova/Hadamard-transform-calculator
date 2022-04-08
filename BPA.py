"Алгоритъм за бързо преобразуване на Адамар (БПА)"

def first_iteration(x):
    y=[]
    
    # За тези, които се събират
    for i in range(4):   
        element = x[i]+x[i+4]
        y.append(element) 
 
    # За тези, които се изваждат
    for i in range(4):   
        element = x[i]-x[i+4]
        y.append(element) 

    return y

def second_iteration(x):
    'x - входен вектор. В нашият случай това ще е y от първата итерация'

    y=[]
    'Правим 4 цикъла защото таблицата тук започва да се дели на 4'
      
      # За тези, които се събират - част 1
    for i in range(2):   
        element = x[i] + x[i+2]
        y.append(element) 
 
      # За тези, които се изваждат - част 1
    for i in range(2):   
        element = x[i] - x[i+2]
        y.append(element) 
    #==========================================================#
      # За тези, които се събират - част 2
    for i in range(4,6):   
        element = x[i] + x[i+2]
        y.append(element) 
 
      # За тези, които се изваждат - част 2
    for i in range(4,6):   
        element = x[i] - x[i+2]
        y.append(element) 

    return y

def third_iteration(x):
    'x - входен вектор. В нашият случай това ще е y от втората итерация'

    y=[]
    'Правим 8 цикъла защото таблицата тук започва да се дели на 4'
      
      # За тези, които се събират - част 1
    for i in range(0,1):   
        element = x[i] + x[i+1]
        y.append(element) 
 
      # За тези, които се изваждат - част 1
    for i in range(0,1):   
        element = x[i] - x[i+1]
        y.append(element) 
    #==========================================================#
      # За тези, които се събират - част 2
    for i in range(2,3):   
        element = x[i] + x[i+1]
        y.append(element) 
 
      # За тези, които се изваждат - част 2
    for i in range(2,3):   
        element = x[i] - x[i+1]
        y.append(element) 
     #==========================================================#
      # За тези, които се събират - част 3
    for i in range(4,5):   
        element = x[i] + x[i+1]
        y.append(element) 
 
      # За тези, които се изваждат - част 3
    for i in range(4,5):   
        element = x[i] - x[i+1]
        y.append(element) 
     #==========================================================#
      # За тези, които се събират - част 2
    for i in range(6,7):   
        element = x[i] + x[i+1]
        y.append(element) 
 
      # За тези, които се изваждат - част 2
    for i in range(6,7):   
        element = x[i] - x[i+1]
        y.append(element) 
    
    return y

def re_order(y):
    "Право преобразуване"
    
    original_elements=y
    reordered_elements=[None]*8

    reordered_elements[0]=original_elements[0]
    reordered_elements[7]=original_elements[1]
    reordered_elements[3]=original_elements[2]
    reordered_elements[4]=original_elements[3]
    reordered_elements[1]=original_elements[4]
    reordered_elements[6]=original_elements[5]
    reordered_elements[2]=original_elements[6]
    reordered_elements[5]=original_elements[7]

    return reordered_elements

def back_re_order(y):
    "Обратно преобразуване"
    
    original_elements=y
    reordered_elements=[None]*8

    reordered_elements[0]=original_elements[0]
    reordered_elements[1]=original_elements[7]
    reordered_elements[2]=original_elements[3]
    reordered_elements[3]=original_elements[4]
    reordered_elements[4]=original_elements[1]
    reordered_elements[5]=original_elements[6]
    reordered_elements[6]=original_elements[2]
    reordered_elements[7]=original_elements[5]

    return reordered_elements
