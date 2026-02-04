#个人收支记账小程序（找豆包出的练手题）
#核心功能：
#1.支持录入「收入 / 支出」类型、金额、备注（比如 “支出 - 20 - 奶茶”“收入 - 100 - 兼职”）；
#2.输入校验（金额必须是数字，类型只能是 “收入 / 支出”）；
#3.统计功能：总收支、总收入、总支出、收支差额；
#4.异常处理：空数据、非法输入、中途退出都不报错；
#5.友好输出：排版清晰，优化视觉效果。

income=[]
expenditure=[]

def check_input(category):   #write_in()函数里用到的检查函数
    # ===================== 核心坑点注释 =====================（豆包友情提供）
    # 【问题】：最初用全局唯一字典example存储记录，所有append操作都指向同一个字典对象，
    #         后续修改example会覆盖列表中所有历史记录（“引用覆盖”）。
    # 【解决措施】：每次录入记录时，通过record = {...}新建独立字典对象，而非复用旧字典。
    # 【底层原因】：Python字典是引用类型，变量名（如record）只是"标签"，列表存储的是内存对象本身；
    #            每次新建字典会在内存中生成新对象，标签record仅指向新对象，旧对象仍保存在列表中，
    #            彻底避免修改新对象时覆盖旧记录。
    # ========================================================
    count=0
    while True:
        print("金额：",end=" ")
        money1=input()
        if money1=="quit":
            print(f"本次共录入{count}条{category}记录")
            break
        try:
            money2=float(money1)
            if money2<=0:
                print("输错了，请输入正数")
            else:
                print("备注：",end=" ")
                ps=input()
                record={
                    "金额":money2,
                    "备注":ps if ps else "无备注"   #三元表达式，有备注用备注，无备注用默认值
                }
                if category=="收入":
                    income.append(record)    #不能用count当作列表索引，因为原列表是空的，这样会报错，所以用append
                else:
                    expenditure.append(record)
                count+=1
                print(f"已完成第{count}次录入")
        except:
            print("输错了，请输入正数")

def write_in():
    print("###先录入收入数据（输入quit结束）：")
    check_input("收入")
    print("###再录入支出数据（输入quit结束）：")
    check_input("支出")
    print("已退出录入功能\n")

def show():
    print("****收入****")
    if not income:
        print("无收入记录")
    else:
        index=1
        for element in income:
            print(f"{index}.  {element["金额"]},{element["备注"]}")
            index+=1
    print("\n****支出****")
    if not expenditure:
        print("无支出记录")
    else:
        index=1
        for element in expenditure:
            print(f"{index}.  {element["金额"]},{element["备注"]}")
            index+=1
    print("============")
    in_sum=sum(record["金额"] for record in income)if income else 0.00      #遍历列表中的字典的某一键值对，且考虑到数据为空的情况
    ex_sum=sum(record["金额"] for record in expenditure)if expenditure else 0.00
    minus=in_sum-ex_sum
    print(f"收入金额为{in_sum:.2f}，支出金额为{ex_sum:.2f}，收支差额为{minus:.2f}")#保留小数点后两位
    print("按任意键退出展示功能")
    input()

#以下是主程序↓↓↓
def main():
    while True:
        print("***这是个人收支统计系统***")
        print("1.录入数据\n2.展示数据\n3.退出系统")
        try:
            num=int(input("请输入对应数字即可跳转："))
            #int()对字符串形式的小数（比如"1.5"）会直接报错，可以进入except中（前提是该语句在try块内）
            match num:
                case 1:
                    write_in()
                case 2:
                    show()
                case 3:
                    print("退出系统")
                    break
                case _:
                    print("输错了，请输入1,2,3中的数字：")
        except:
            print("输错了，请输入1,2,3中的数字：")

"""
    【封装主程序核心说明】（豆包总结）：
    1. 定义：将while True主循环封装到main()函数，而非直接写在全局；
    2. 触发：通过if __name__ == "__main__"调用main()；
    3. 核心好处：
       - 避免在其他程序中导入本程序模块时意外执行主循环（如import account时不会启动记账系统）；
       - 代码结构分离：函数（功能模块）和main()（执行逻辑）清晰区分；
       - 方便调试：可单独调用函数（如show()），无需运行整个主程序；
    4. __name__特性：
       - 直接运行文件时，__name__ = "__main__" → 执行main()；
       - 导入文件时，__name__ = 模块名 → 不执行main()。
    """
if __name__ == "__main__":
    main()


        






    
