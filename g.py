msg_ = ("Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don\'t be silly! It\'s just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)")

memory = 0


def is_one_digit(v):
    if v > -10 and v < 10 and type(v) is int:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]

    if v1 == 1 or v2 == 1 and v3 == '*':
        msg = msg + msg_[7]

    if v1 == 0 or v2 == 0 and v3 in '+-*':
        msg = msg + msg_[8]

    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def in_put(a):
    if a == "M":
        a = memory
        return a
    try:
        a = int(a)
    except ValueError:
        a = float(a)
    return a


def ostatok(a):
    if a % int(a) == 0:
        return int(a)
    return a


while True:
    print(msg_[0])
    x, oper, y = input().split()

    try:
        x = in_put(x)
        y = in_put(y)

        x = ostatok(x)
        y = ostatok(y)


    except ValueError:
        print(msg_[1])
        continue

    if oper not in '+-*/':
        print(msg_[2])
        continue

    check(x, y, oper)

    if oper == '+':
        result = x + y

    elif oper == '-':
        result = x - y

    elif oper == '*':
        result = x * y

    elif oper == '/':
        try:
            result = x / y

        except ZeroDivisionError:
            print(msg_[3])
            continue

    print(float(result))

    while True:
        print(msg_[4])
        answer = input()
        if answer == 'y':
            if is_one_digit(result) is True:
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    answer_3 = input()
                    if answer_3 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        memory = result
                        break
                    break
                break
            memory = result
            break
        break

    print(memory)
    print(msg_[5])
    answer_2 = input()

    if answer_2 == 'y':
        continue

    break
