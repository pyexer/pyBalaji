# Python code to count the number of occurrences
x=int(input("enter the number:"))
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


lst = [8, 6, 8, 10, 8,45 ,324 ,1 ,1 ,3 ,3 ,5 , 20, 10, 8, 8]

print('{} has occured {} times'.format(x, countX(lst, x)))
