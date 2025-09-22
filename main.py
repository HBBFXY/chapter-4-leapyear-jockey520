try:
    year = eval(input("请输入年份："))
    if year%4 ==0:
        if year % 400 == 0:
            print("是闰年")
        elif year % 100 != 0:
            print("是闰年")
        else:
            print("不是闰年")
    else:
        print("不是闰年")
except :
    print("输入错误，请输入一个整数") 在此处编写代码
