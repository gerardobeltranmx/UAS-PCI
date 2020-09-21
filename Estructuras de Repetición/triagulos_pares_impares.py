datos = input()
m,n = datos.split (" ")

n=int(n)
m=int(m)
par =0
impar = 0
for a in range(m,n): 
    for b in range(a,n):
        for c in range (b,n): 
            if (a+b>c) and (a+c>b) and (b+c>a):   
                if(a%2==0) and (b%2==0) and (c%2==0): 
                    par=par+1
                elif  (a%2!=0) and (b%2!=0) and (c%2!=0): 
                    impar=impar+1
                        
print("{0} {1}".fomat(impar, par))
                         