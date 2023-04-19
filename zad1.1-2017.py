#================TESTS=============================
table1= [7,5,11,33]
table2 = [15,12,10,6,5,1]
def zad1(p, tab=[]):
    tabForValue = []   
    for val2 in range(len(tab)):
        for val in range(val2+1, len(tab)):            
            result = tab[val2]*tab[val]
            if result%p==0:                
                pass
            elif result%p!=0:
              tabForValue.append(result)
    BiggestValue = 0
    for value in tabForValue:
        if value > BiggestValue:
            BiggestValue = value       
    return BiggestValue              
print(zad1(7,table2))