def find_location (fullString, search) :
    a = full_name.find(name)
    b = full_name.find(name) + len(name) - 1
    c = [0, 1]
    c[0] = a
    c[1] = b
    return c

def draw_tree():
    x = 0
    while (x < 2):
        x = int(input('请输入你想绘制树的高度，大于1的任意整数：'))
    # print(x)
    # x * 2 - 1
    # no_odd = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    sum_char = x * 2 - 1
    # print(sum_char)
    line = 1
    while (line <= x):
        left = (sum_char - line - line + 1) / 2
        print(int(left) * ' ', end='')
        star = 1
        while (star <= (sum_char - left*2)):
            if((star+1)%2==0):
                print('*', end='')
            else:
                print(' ', end='')
            star+=1
        print(int(left)*' ', end='')
        line += 1
        print('')
    print(int((sum_char - 1) / 2) * ' ' + '|' + int((sum_char - 1) / 2) * ' ',end='')