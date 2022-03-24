a=input("Enter Strings. - Use Space To Seperate Words - : ")
b=[]
for i in a.split():
    if i==i[::-1]: 
        b.append(i)
print()
for i in range(len(b)):
    print(b[i])
print()
print("Total {} Pelindrome Words in String: {}".format(len(b),b)) 
