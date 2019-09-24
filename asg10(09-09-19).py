# Difference between two given list

l1=[5,8,23,67,90]
l2=[3,5,20,60,85]
l3=[]
m=-1
n=0
for i in l1[:]:
    m+=1
    #print(m,"m")
    n+=1
    #print(n,"n")
    for j in l2[m:n]:
        diff=i-j
        l3.append(diff)
print("Difference between list1: {} and list2: {} is {}".format(l1,l2,l3))

