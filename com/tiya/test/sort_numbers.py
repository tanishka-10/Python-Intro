numberlist=[7,10,2,42,3]
(len(numberlist)-1)
for j in range(len(numberlist)-1):
    for i in range(len(numberlist)-1):
        if numberlist[i] > numberlist[i+1]:
            temp = numberlist[i+1]
            numberlist[i+1] = numberlist[i]
            numberlist[i] = temp

    print(numberlist)

print("final list")
print(numberlist)