count = 0
for i in range(0,N):
    if list1[i] != 0:
        list1[count] = list1[i]
        count += 1

for i in range(0, count):
    list2.append(list1[i])
