#figura1
num = 1
for x in range(1, 5):
    print '*' * num
    num += 1
#figura2
num2 = 1
num3 = 3
for x in range(1, 5):
    print ' ' * num3 + '*' * num2
    num2 += 1
    num3 -= 1
#figura3
num4 = 1
num5 = 3
for x in range(1, 5):
    print ' ' * num5 + '*' * num4
    num4 += 2
    num5 -= 1
