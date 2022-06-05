from math import log


def time(x):
    years = x / 12

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

    return answer


def n_mothly_fayments(x, y, z):
    i = z / 1200
    n = log((y / (y - i * x)), i + 1)

    while True:
        if n <= 1:
            print("It will take 1 month to repay this loan!")
            break

        elif 1 < n <= 11:

            if n % 1 != 0:
                n = int(n) + 1

            print(f"It will take {n} months to repay this loan!")
            break

        elif 11 < n < 12:

            if n % 1 != 0:
                n = int(n) + 1

            print("It will take 1 year to repay this loan!")
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

    return


def ann_m_payment_amount(x, y, i):
    return answer


def loan_principal(x, y, i):
    return answer


print(f"""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

answer = input()

if answer == "n":
    print("Enter the loan principal:")
    loan_prin = int(input())
    print("Enter the monthly payment:")
    m_payment = int(input())
    print("Enter the loan interest:")
    loan_int = int(input())

    n_mothly_fayments(loan_prin, m_payment, loan_int)

elif answer == "a":
    print("Enter the loan principal:")
    loan_prin = int(input())
    print("Enter the number of periods:")
    n_periods = int(input())
    print("Enter the loan interest:")
    loan_int = int(input())

    n_mothly_fayments(loan_prin, n_periods, loan_int)

elif answer == "p":
    print("Enter the annuity payment:")
    ann_payment = float(input())
    print("Enter the number of periods:")
    n_periods = int(input())
    print("Enter the loan interest:")
    loan_int = float(input())

    loan_principal(ann_payment, n_periods, loan_int)
