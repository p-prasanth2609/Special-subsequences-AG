a=input()
count_A=0
result=0
for i in range(len(a)):
    if(a[i]=='A'):
        count_A+=1
    if(a[i]=='G'):
        result+=count_A
print(result)
