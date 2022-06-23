from math import log

p = 500000
n = 120
interest = 7.8
i = interest / (12 * 100)
annuity_payment = 23000


def d_m(x, y, z):
    payed = 0

    for m in range(1, y + 1):
        payment = x / y + z * (x - x * (m - 1)/y)
        if payment % 1 != 0:
            payment += 1
        payed += int(payment)
        print(f"Month {m}: payment is {int(payment)}")

    print(f"Overpayment = {int(payed - x)}")


def annuity(x, y, z):
    ann = x * (z * (1 + z) ** y) / ((1 + z) ** y - 1)
    if ann % 1 != 0:
        ann += 1
    print(f"Your annuity payment = {int(ann)}!")
    print(f"Overpayment = {int(ann) * y - x}")


def loan_prin(x, y, z):
    principal = x / ((z * (1 + z) ** y) / ((1 + z) ** y - 1))
    print(f"Your annuity payment = {int(principal)}!")
    print(f"Overpayment = {x * y - int(principal)}")


def n_payments(x, y, z):
    n = log((y / (y - x * z)), x + 1)

    def time(a):
        years = a / 12

        while 1 < years < 2:
            if years % 1 != 0:
                months = int(x) - 11

                if months == 1:
                    print("It will take 1 year and 1 month to repay this loan!")
                    break
                print(f"It will take 1 year and {int(months)} months to repay this loan!")
                break

            months = x - 12
            if months == 1:
                print("It will take 1 year and 1 month to repay this loan!")
                break
            print(f"It will take 1 year and {int(months)} months to repay this loan!")
            break

        while years > 2:
            if years % 1 != 0:
                months = int(x) + 1

                if months == 1:
                    print(f"It will take {int(years)} years and 1 month to repay this loan!")
                    break
                print(f"It will take {int(years)} years and {months - int(years) * 12} months to repay this loan!")
                break

            if months == 1:
                print(f"It will take {int(years)} years and 1 month to repay this loan!")
                break
            print(f"It will take {int(years)} years and {months - int(years) * 12} months to repay this loan!")
            break

    while True:
        if n <= 1:
            print("It will take 1 month to repay this loan!")
            break

        elif 1 < n <= 11:

            if n % 1 != 0:
                n = int(n) + 1

            print(f"It will take {n} months to repay this loan!")
            break

        elif 11 < n < 12 or 23 < n < 24:

            if n // 1 == 11:
                print("It will take 1 year to repay this loan!")
                n = 12
                break
            print("It will take 2 years to repay this loan!")
            n = 24
            break

        elif n % 12 == 0:
            if n / 12 == 1:
                print("It will take 1 year to repay this loan!")
                break
            print(f"It will take {int(n / 12)} years to repay this loan!")
            break

        else:
            time(n)
            break

    print(f"Overpayment = {y * n - z}")

# d_m(p, n, i)
# annuity(p, n, i)
# loan_prin(annuity_payment, n, i)
# n_payments(i, annuity_payment, p)
# 1,2,4,5,6
