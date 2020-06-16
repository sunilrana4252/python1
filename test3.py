s=input("enter a sentence")
a=s.split()
d={}
for i in a:
    d[i]=d.get(i,0)+1
# print(d)
for k,v in d.items():
    print("{} occurs {} times ".format(k,v))
