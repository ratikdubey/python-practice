tpl1 = (1,2,3,4,5,6,7,8,9)

tpl2 = tpl1[:-1]
print(tpl2)

tpl3 = (10,) + tpl2
print(tpl3)

tpl4 = tpl3[:3] + (11,) + tpl3[3:]
print(tpl4)