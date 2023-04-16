lb = []
while True :
    zx = input("查看输入1,添加输入2,删除输入3,退出输入4")
    zxint = int(zx)
    if zxint == 1:
        print(lb)
    elif zxint == 2:
        zx = input("输入要添加的元素")
        lb.append(zx)
    elif zxint == 3:
        zx = input("输入要删除的元素")
        lb.remove(zx)
    elif zxint == 4:
        break
print("已退出")