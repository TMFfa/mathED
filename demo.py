# print('x:\t0\t1\t2\t3\t')
# print('p:\t0.125\t0.125\t0.25\t0.5')

#制表符的写法是\t，作用是对齐表格的各列。
# print("I'm Bob,what is your name?")
# print("I'm Bob,\twhat is your name?")


from fractions import Fraction
# print(Fraction(1))
# print(Fraction(1.1))
# print(Fraction(1.1) == 11/10)


def num(rx, rp):
    x, p = [], []
    for i in rx:
        x.append(Fraction(i))
    for i in rp:
        p.append(Fraction(i))
    return x, p


def input_():
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


x, p = input_()