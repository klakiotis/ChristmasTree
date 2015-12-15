print("As ftiaksoume ena x-mass tree. Dwse diastaseis dentrou")
ypsos_dentrou=input("Dwse to ypsos tou dentrou:")
platos_kormou=input("Dwse to platos tou kormou tou dentrou: ")
ypsos_kormou=input("Dwse to ypsos tou kormou tou dentrou: ")
n=ypsos_dentrou
x=ypsos_kormou 
z=platos_kormou
i=0
while i < n:
 print((" " * (n - i)) + ("*" * (i * 2 + 1)))
 i = i + 1
j = 0
while j < x:
 print(' ' * int((2*n-1)/2) + '*' * z + ' ' * ((2*n-1)/2))
 j = j + 1 
