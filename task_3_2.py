import random
a=['clubs','diamonds','hearts','spades']
b=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card=[]
color=random.choice(a)
value=random.choice(b)
card=[color,value]
print(card)
print(color,value,sep='-')