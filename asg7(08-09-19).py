#pyhton code to find the occurrence of the each char in a word

n=input("enter any word:")
for i in n[:]:
    t=i
    j=0
    for i in n[:]:
        if(t==i):
            j=j+1

    print("count of {} is {}".format(t,j))

    

