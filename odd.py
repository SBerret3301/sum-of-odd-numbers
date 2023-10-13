x = int(input("enter a number : "))
y = 1
s = 0
for i in range(1 , x + 1) :
    s = s + pow(y , 2)
    y = y + 2
print(s)