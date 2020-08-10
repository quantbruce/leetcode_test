while True:
    try:
            m,n = list(map(int, input().split()))
            num, res = 0, []
            for i in range(m, n+1):
                x = i//100
                y = i//10%10
                z = i%10
                if x**3+y**3+z**3 == i:
                    num += 1
                    res.append(i)
            if num!=0:
                for i in range(len(res)):
                    if i==len(res)-1:
                        print(res[i]) # 输出的最后一个数是不带' '的
                    else:
                        print(res[i], end=' ') # 细节啊
            else:
                print('no')
    except:
        break
        
        
        
        
