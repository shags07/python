def remove(array):
   i = 0
   while i < len(array):
      j = i + 1
      while j < len(array):
         if array[i] == array[j]:
            del array[j]
         else:
            j += 1
      i += 1
array = ['A','B','a','C','A','a'] 
remove (array)
print(array)
