
l=str.split()
str=inputStr
s=rotateHow
if s[0]=='L':
    for i in range(len(l)):
        k=int(s[1])
        l[i]=l[i][k:]+l[i][:k]
else:
    for i in range(len(l)):
        l[i]=l[i][len(l[i])-int(s[1]):]+l[i][:len(l[i])-int(s[1])]

ans=""
for i in l:
    ans+=i+" "

print(ans)