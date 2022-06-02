msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?"
msg_3 = "Yeah... division by zero. Smart move..."

while True:
    print(msg_0)
    x, oper, y = input().split()

    try:
        x = float(x)
        y = float(y)

    except ValueError:
        print(msg_1)
        continue

    if oper not in '+-*/':
        continue

    try:
        result = eval(str(x) + oper + str(y))
        print(result)
        break
    except ZeroDivisionError:
        print(msg_3)
        continue
