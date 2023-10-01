for i in range(0,100):
    i+=1
    
    if i%3 == 0 and i%5==0:
        print('CracklePop')
    elif i % 3 == 0:
        print('Crackle') 
    elif i % 5 == 0:
        print('Pop')
    else: 
        print(i)
   