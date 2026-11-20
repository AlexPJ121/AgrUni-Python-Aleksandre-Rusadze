while True:
  n = int(input('შეიყვანე რიცხვი 1-100: '))
  if n>=1 and n<=100:
    break
  print("რიცხვი არ არის 1-100 შუალედში! თავიდან სცადე.")
numb = [0, 1]
for i in range(2, n):
  numb.append(numb[i-1] + numb[i-2])
if n==1:
  print(numb[0])
else:
  print(numb)