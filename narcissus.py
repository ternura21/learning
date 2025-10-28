
for i in range(100,1000):
    a = i % 10
    c = i // 100
    b =i//10%10
    if(a*a*a+b*b*b+c*c*c==i):



        print('水仙花数为',i)

    i=i+1



