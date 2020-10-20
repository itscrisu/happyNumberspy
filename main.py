def esNumFeliz(n):    
    res = sum = 0    
    while(n > 0):    
        res = n % 10 
        sum = sum + (res * res)    
        n = n // 10   
    return sum    
        
num = int(input("Ingresá un número: "))    
resultado = num    
     
while(resultado != 1 and resultado != 4):    
    resultado = esNumFeliz(resultado)   
     
if(resultado == 1):    
    print(num, " es un número feliz :)")   
else:    
    print(num, " no es un número feliz :(")