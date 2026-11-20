first=input('first word/str: ')
second=input('second word/str: ')
characters=('abcdefghijklmnopqrstuvwxyz')
a=list(first.lower())
b=list(second.lower())
c=[]
d=[]
for i in range(len(a)):
  if a[i] in characters:
    c.append(a[i])
  else:
    continue
for i in range(len(b)):
  if b[i] in characters:
    d.append(b[i])
  else:
    continue
e=set(c)
f=set(d)
if e==f:
  print('YES')
else:
  print('NO')