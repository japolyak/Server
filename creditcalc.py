import sys
import argparse
from math import log


args = sys.argv

if len(args) < 5:
    print("Incorrect parameters.")

parser = argparse.ArgumentParser()

parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="You need to choose only one option from the list.")


parser.add_argument("--principal", default=0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0)
parser.add_argument("--payment", default=0)

args = parser.parse_args()

values = [float(args.principal),
          int(args.periods),
          float(args.interest),
          float(args.payment)]

for i in values:
    if i < 0:
        print("Incorrect parameters.")


while True:

    if args.type == "diff" and args.payment != 0:
        print("Incorrect parameters.")
        break

    elif args.type == "diff" and args.payment == 0:
        def d_m(x, y, z):
            payed = 0

            for m in range(1, y + 1):
                payment = x / y + z * (x - x * (m - 1)/y) / 1200
                if payment % 1 != 0:
                    payment += 1
                payed += int(payment)
                print(f"Month {m}: payment is {int(payment)}")

            print(f"Overpayment = {int(payed - x)}")
        d_m(values[0], values[1], values[2])
        break

    elif args.payment == 0 and args.interest != 0:
        def annuity(x, y, z):
            ann = x * (z / 1200 * (1 + z / 1200) ** y) / ((1 + z / 1200) ** y - 1)
            if ann % 1 != 0:
                ann += 1
            print(f"Your annuity payment = {int(int(ann) * y - x)}!")
            print(f"Overpayment = {int(ann)}")
        annuity(values[0], values[1], values[2])
        break

    elif args.principal == 0 and args.interest != 0:
        def loan_prin(x, y, z):
            principal = x / ((z / 1200 * (1 + z / 1200) ** y) / ((1 + z / 1200) ** y - 1))
            print(f"Your annuity payment = {int(principal)}!")
            print(f"Overpayment = {int(x * y - int(principal))}")
        loan_prin(values[3], values[1], values[2])
        break

    elif args.periods == 0 and args.interest != 0:
        def n_payments(x, y, z):
            n = log((y / (y - x * z / 1200)), x / 1200 + 1)

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
                        print(
                            f"It will take {int(years)} years and {months - int(years) * 12} months to repay this loan!")
                        break

                    if months == 1:
                        print(f"It will take {int(years)} years and 1 month to repay this loan!")
                        break
                    print(f"It will take {int(years)} years and {months - int(years) * 12} months to repay this loan!")
                    break

            while True:
                if n <= 1:
                    print("It will take 1 month to repay this loan!")
                    n = 1
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
                        n = 12
                        break
                    print(f"It will take {int(n / 12)} years to repay this loan!")
                    break

                else:
                    time(n)
                    break

            print(f"Overpayment = {int(y * n - z)}")
        n_payments(values[2], values[3], values[0])
        break

    else:
        print("Incorrect parameters.")
        break
