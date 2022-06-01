msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?"

Operators = ('+', '-', '*', '/')

a = True

while a is True:
    print(msg_0)
    calc = input()
    calc = calc.split()
    try:
        x = float(calc[0])
        y = float(calc[2])
        oper = calc[1]

        for i, r in enumerate(Operators):
            print(r)
            if oper == r:
                break
            print(i)
        print(msg_2)
        a = True

    except ValueError:
        print(msg_1)
        a = True
