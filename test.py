a=input("enter a sentence: ")
output=''
output1=''
output2=''
i=0-len(a)
while i<=-1:
    if a[i]==' ':
        output1=output+' '+output1
        output = ' '

    else:
        output=output+a[i]
    i+=1
output2=output+' '+ output1
print(output2)