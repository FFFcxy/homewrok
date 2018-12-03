n = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if c != b and b != a and c != a:
                n += 1
                d = a*100+b*10+c
                print('第%d个数为%d'%(n,d))
