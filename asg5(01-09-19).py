#python code to concatenate the elements in a list as a string

def concatenate(l):
    result= ''
    for items in l:
        result += items
    return result



l=["b","a","l","a","j","i"]
print(concatenate(l))
