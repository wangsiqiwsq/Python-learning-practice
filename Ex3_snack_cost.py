print("请输入最近几天零食花费金额（输入quit即停止）：")
snack_cost=[]
day=add=count=0     #连续赋值的写法（不能用逗号）
while True:
    day+=1
    print(f"第{day}天金额：",end=" ")
    cost1=input()
    if cost1=="quit":
        break
    try:
        cost2=float(cost1)
        if cost2>10:
            count+=1
        snack_cost.append(cost2)
    except:
        print("输入内容不是数字，请重新输入")
        day-=1     #防止天数在输错内容的情况下依旧增多
if snack_cost:     #判断一下列表里有没有数据，避免计算时因空数据而出错
    add=sum(snack_cost)#python中自带求和函数sum()
    average=add/len(snack_cost)
    print("\n统计结果如下：")
    print(f"最近几天零食花销总和为{add}")
    print(f"花销平均值（保留一位小数）为{average:.1f}")#.1f->保留一位小数
    print(f"其中花销大于10的天数共有{count}天")
else:
    print("\n你还没有输入任何数据哦")
