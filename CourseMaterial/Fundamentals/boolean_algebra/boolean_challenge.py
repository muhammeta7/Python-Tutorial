# lobster =
# rabbit =
# bird = ???
# lion = True
# cat = ???
# pig = False
# bison = ???
# eagle = ???
# bear = False
# chicken = True
# monkey = True
# pony = ???
# fish = True
# dolphin = False
# turkey = ???
# spider = False
# snake = False
# ape = True
# dog = True
# cow = True
# wolf = False
# horse = ???
# deer = True
# shark = True
#
# print(((dog and lion) and (snake and dog) or (lobster and fish) or (cow and ape)) == True)
# print(((cat or bear) or (dog and shark) and (chicken and monkey) or (lion or deer)) == True)
# print(((not spider and pig) or (not bird or not turkey) or (dog and bear) and (wolf and lion)) == True)
# print(((lobster and dolphin) and (eagle and monkey) and (lion and rabbit) and (rabbit and dolphin)) == False)
# print(((wolf or rabbit) and (not eagle and bird) or (dog and dolphin) and (turkey and pig)) == False)
# print(((fish and bison) and (not horse or lion) or (pony and spider) or (not bear and pig)) == True)
# print(((snake and not ape) and (cat and wolf) and (deer and wolf) or (bird or wolf)) == False)
# print(((shark and wolf) and (spider and not turkey) and (turkey and rabbit) or (eagle or shark)) == True)
# print(((dolphin and bird) or (dog or lobster) and (not fish and bear) and (not snake and fish)) == False)
# print(((pony and snake) and (rabbit or snake) and (shark or horse) and (cat or bird)) == False)

# All print statements should return True



# TODO #######################################################################################################
# TODO Return integers for each to make this work. HINT: Range should not be -1,0,1 but more 1-100.
# I tried to take the statements with all the ands and group them. There's so many unknowns and I guess my algorithmic skillset
# is still not the best yet. It feels like linear algebra from the little I remember from that class. There's just a lot more conditions
# that factor in.

# a1 = ???
# d4 = ???
# q8 = ???
# r9 = ???
# l3 = ???
# z8 = ???
# b2 = ???
# g7 = ???
# o6 = ???
# m4 = ???
# k2 = ???
# j1 = ???
# e5 = ???
# v4 = ???
# p7 = ???
# s1 = ???
# f6 = ???
# c3 = ???
# u3 = ???
# x6 = ???
# w5 = ???
# h8 = ???
# i9 = ???
# t2 = ???
# y7 = ???

"(b2 > z8) and (h8 <= l3) and (j1 <= w5) and (o6 <= j1) evaluates to False"
"(w5 < c3) and (l3 == f6) or (r9 != i9) or (q8 > d4) evaluates to True"
"(p7 <= a1) or (i9 > z8) and (q8 != j1) or (a1 > d4) evaluates to True"
"(g7 == z8) and (k2 > b2) and (d4 < r9) or (g7 < x6) evaluates to False"
"(g7 != p7) and (m4 > y7) or (g7 >= i9) or (y7 != b2) evaluates to True"
"(h8 != x6) and (p7 < a1) and (z8 == v4) and (h8 == e5) evaluates to False"
"(h8 >= f6) and (p7 > x6) and (z8 < g7) and (o6 < b2) evaluates to False"
"(b2 != r9) and (g7 >= z8) and (q8 >= c3) or (u3 > d4) evaluates to True"
"(p7 > s1) or (p7 != z8) and (q8 != b2) or (t2 <= u3) evaluates to True"
"(g7 < v4) or (p7 >= s1) and (g7 < t2) or (p7 != s1) evaluates to True"


# TODO #######################################################################################################
# TODO Explain how this works, haven't even looked at it yet.
dpz = 12
tkn = 85
nol = 11
vnh = 24
trb = 20
zmm = 82
print((zmm == trb) or (nol < dpz) or (nol > tkn) and (vnh == trb)) # evaluates to True
print(f'{(zmm == trb)} or {(nol < dpz)} or {(nol > tkn)} and {(vnh == trb)}')
print(False or True or False and False)

