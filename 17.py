# Задача 17: 
# Дан список чисел. Определите, сколько в нем встречается разных чисел.
# Input: [1,1,2,0,-1,3,4,4]
# Output: 6

#Первый способ
list = [1, 1, 2, 0, -1, 3, 4, 4]
list1 = set(list)
print(len(list1))


#Второй способ
list = [1, 1, 2, 0, -1, 3, 4, 4]
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
print(len(list1))



