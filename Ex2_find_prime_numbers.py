print("请输入一个正整数，将输出小于等于它的全部质数：")
while True:
    try:
        num=int(input())
        if num>0:
            break
        else:
            print("不要输入0或负数哦，请重新输入一个正整数:")
    except:
        print("不要输入其他内容哦，请重新输入一个正整数:")
if num<2:
    prime=[]
else:
    prime=[2]
    for i in range(3,num+1,2):#跳过偶数，效率更高
        index=1
        for j in range(3,int(i**0.5)+1,2):#跳过偶数的除数
            if i%j==0:
                index=0
                break
        if index==1:
            prime.append(i)
        #不需要i+=2了，本来for语句里就包含了。。

print(f"小于等于{num}的全部质数有{prime}")
