# 接受三角形三边，判断三角形形状

while True:
    try:
        a, b, c = map(float, input("输入三角形三边（以空格隔开）： ").split())
    except:
        print("输入有误，请重新输入\n")
    else:
        if(a + b <= c or a + c <= b or b + c <= a):
            print("输入的三边边长构不成三角形\n")
        else:
            if (a == b and a == c):
                print("是等边三角形\n")
            elif(a == b or a == c or b == c):
                print("是等腰三角形\n")
            else:
                print("普通三角形\n")
