char="1234abcd"
a=list(char)
i=0
b=[]
while i<len(a):
    c=a[-1-i]
    b.append(c)
    i=i+1
d="".join(b)
print(d)
    
