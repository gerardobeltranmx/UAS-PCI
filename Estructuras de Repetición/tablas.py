N = int(input())

for j in range(0, N): 
    num = int(input())
    for i in range(1,11): 
        c= num*i
        print("%dx%d=%d" % (num, i, c))

    print()   


