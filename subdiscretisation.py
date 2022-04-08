"Кодиране по субдискретизация"

def subdiscretisation(y):
    'y -> трансформантата'
    
    for i in range(len(y)):
        for l in range(0,8):
            if(i==2*l):
                continue
            if(i==2*l+1):
                y[i]=0
    return y


def interlocation(y_coded_by_subdiscretisation):
   
    l=0
    while l <= 3:
        if(l==3):
            answer = (y_coded_by_subdiscretisation[2*l])/2
        else:
            answer = (y_coded_by_subdiscretisation[2*l]+y_coded_by_subdiscretisation[2*l+2])/2
        y_coded_by_subdiscretisation[2*l+1]= answer
        l += 1
    
    return y_coded_by_subdiscretisation
