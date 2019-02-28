def sort_words(str1):
    list1=str1.split(",")
    list2=[]
    list1=sorted(list1)
    for i in list1:
        if i not in list2:
            list2.append(i)
    
    return ",".join(list2)

print(sort_words("kangaroo,rabbit,mouse,ant,mouse,ant"))
