start = int(input("Enter your starting number: "))
size = int(input("Enter your sequence size: "))

seq = [] 
out = ""
for i in range(0,size):
    
    if i == 0 or i == 1:
        seq.append(start)
    else:
        seq.append(seq[i-1] + seq[i-2])
    out += str(seq[i]) + " "
    
print(out)








