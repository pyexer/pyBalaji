#program to find the smallest integer in a given list.


l=[67,7,3,8,5,9]
for i in l:
    for j in l:
        if(i>j):
            temp=i
            i=j
            j=temp


print (i)
