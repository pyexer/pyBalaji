#python code to find the given character is vowel or not.
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print("{} is a vowel".format(ch))
else:
    print("{} is not a vowel".format(ch))
