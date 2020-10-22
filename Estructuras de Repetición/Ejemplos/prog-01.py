def anagrama(x1, x2):
    v1 = [0 for i in range(26)]
    v2 = [0 for i in range(26)]
    correcto = True
    if len(x1) == len(x2):
        for j in range(len(x1)):
            a = ord(x1[j - 1])-97
            b = ord(x2[j - 1])-97
            v1[a] += 1
            v2[b] += 1
        print(v1)
        print(v2)

        if v1 == v2:
            correcto = True
        else:
            correcto= False

    return correcto


N = int(input())

for i in range(1, N+1):
    a,b=input().split(' ')
    if anagrama(a, b)==False:
        print('no')
    else:
        print('si')