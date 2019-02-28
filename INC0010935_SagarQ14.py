def quadratic(array):
    list11=array.split(",")
    list2=[]
    k= 0
    N= k*(k+1)/2
    for i in list11:
        while k==N:
            N =k-1
            abc=list11.pop(N)
        list2.append(abc)
        list2.sort[0:k,N-k]
        
    return ",".join(list2)
print(quadratic([8, 9, 11, 1, 1, 1, 45, 3, 2, 4, 13, 13]))
