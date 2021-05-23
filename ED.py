from fractions import Fraction
# 参考：https://www.jianshu.com/p/6073b6ecc1e5
def E(x, p):  # args are list
    sum = 0
    for i in range(len(x)):
        sum += x[i] * p[i]
    print('E(X)=', sum, '   or', float(sum))
    return sum


def D(x, p):
    e = E(x, p)
    sum = 0
    for i in range(len(x)):
        sum += ((x[i]-e)**2)*p[i]
    print('D(X)=', sum, '   or', float(sum))
    return sum

"""
以前版本，已重写
def num(number):
    if '/' in number:
        n = number.split('/')
        return int(n[0]) / int(n[1])
    else:
        return float(number)


def input_():
    x = []
    p = []
    rx = []
    rp = []
    first_input = input('输入分布列：')
    if ' ' in first_input:
        li = first_input.split(' ')
        for i in li:
            x_i = num(i.split(',')[0])
            p_i = num(i.split(',')[1])
            x.append(x_i)
            p.append(p_i)
            rx.append(i.split(',')[0])
            rp.append(i.split(',')[1])
    else:
        lix = first_input.split(',')
        for i in lix:
           x.append(num(i))
           rx.append(i)
        second_input = input('请输入随机变量对应的概率：')
        lip = second_input.split(',')
        for i in lip:
            p.append(num(i))
            rp.append(i)
    print('X'.center(5), end='|')
    for i in rx:
        print(i.center(5), end='|')
    print('\n', '-'*(len(rx)*6+6), sep='')
    print('p'.center(5), end='|')
    for i in rp:
        print(i.center(5), end='|')
    print('\n')
    return x, p
"""


def num(rx, rp):
    """
    这里用分数表示所有数，Fraction太强了，小数，整数，字符串数字都能转成分数，处理这种输入的数字极其方便
    """
    x, p = [], []
    for i in rx:
        x.append(Fraction(i))
    for i in rp:
        p.append(Fraction(i))
    return x, p


def input_():
    """
    这个没有用自定义对齐了，直接用\t制表符，其实它相当于'str'.ljust(8)
    """
    rx, rp = [], []
    first_input = input('请输入分布列：')
    if ';' in first_input:
        li = first_input.split(';')
        for i in li:
            rx.append(i.split(',')[0])
            rp.append(i.split(',')[1])
    else:
        rx = first_input.split(',')
        second_input = input('请输入随机变量对应概率：')
        rp = second_input.split(',')
    
    x, p = num(rx,rp)

    if sum(p) != 1:
        print('分布列概率和不为1')
        input_()
    else:
        print('X:', end='')
        for i in rx:
            print(f'\t{i}', end='')
        print('\np:', end='')
        for i in rp:
            print(f'\t{i}', end='')
        print('\n')
        return x, p


# x = [1, 2, 3]
# p = [0.4, 0.2, 0.4]
x, p = input_()
D(x, p)
