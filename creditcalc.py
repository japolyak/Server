P = 500000
n = 120
interest = 5.6
i = interest / (12 * 100)
annuity_payment = 8722


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


def n_payments():


# d_m(P, n, i)
# annuity(P, n, i)
# loan_prin(annuity_payment, n, i)
#1,2,4,5