word = input('write the word you want to check: ')
a='abcdefghijklmnopqrstuvwxyz'
characters=list(word.lower()) #pirveli uppercasedan 'dacva'
letters=[]
for i in range(len(characters)):
  if characters[i] in a:
    letters.append(characters[i])
if letters == letters[::-1]:
  print('is palindrome')
else:
  print('is not palindrome')