import random

print()
print('WORK1.0')
print()
choose = int(input('Please enter the level of difficulty(1~10):'))
while choose<1 or choose > 10:
	print('Set failed')
	choose = int(input('Please enter the level of difficulty(1~10):'))
choose_2 = int(20 / choose)
print(choose*choose_2,'question')

point_bocd = 0

u = 1

l = 2
m = 11
L = 2
M = 11


for i in range(choose):
    for n in range(choose_2):
        a = random.randint(l+choose**2,m+choose**2)
        b = random.randint(L+choose**2,M+choose**2)
        l = l + u * (i + choose)
        m = m + u * (i + choose)
        L = L + u * (i + choose)
        M = M + u * (i + choose)
        c = a + b
        print(a,'+',b,'=','?')

        answ = int(input('The answer:'))

        if(answ == c):
            point_bocd = point_bocd + 1

        else:
            point_bocd = point_bocd

print('Accuracy rate：',(point_bocd / int((choose*choose_2))*100),'％')

input()
