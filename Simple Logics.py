### Binary to Integer
a1 = 111
count = 0
while  a1 > 0:
    count = (count * 2) + a1 % 10
    a1 //= 10
print("Binary ",a1 ," to Integer ",count)


### Integer to Binary
a2 = 7
b2 = bin(a2)[2:]
print("Integer ",a2, " to Binary ",b2)


### Roman to Integer
arr = "MCMXVII"
def RomanToInteger(s):
    dct = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000 , "IV":4 , 
    "IX":9 , "XL":40 , "XC":90 , "CD":400 , "CM":900}
    lst = []
    i = 0
    j = len(s)
    new = ""
    while i < j:
        if s[i:i+2] in dct:
            new = s[i:i+2]
            lst.append(dct[new])
            i += 2
        elif s[i] in dct:
            lst.append(dct[s[i]])
            i += 1
    return sum(lst)


### Mirror Tree Logic
def mirror(root):
    if root is None:
        return None
    root.left , root.right = root.right , root.left
    mirror(root.left)
    mirror(root.right)
    return root
