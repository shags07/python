def find_pairs(array,n):
    leng=len(array)
    for i in range(leng): 
        for j in range(leng):
            for k in range(leng):
                if (array[i] + array[j] + array[k] == n):
                    print("(" , array[i], ", ", array[j],", ", array[k],")", sep = "") 
find_pairs([1,5,7,8,9,6,10,12,4,-5],10)

