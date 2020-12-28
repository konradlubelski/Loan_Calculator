import argparse
import math

#function which check number of arguments
def count_true(list_):
    counter = 0
    for a in list_:
        if a:
            counter += 1
    return counter

#function wchich check that all arguments in list_ are positive
def posivite_numbers(list_):
    for a in list_:
        if a <= 0:
            print("Not all loan parameters are positive.")
            return False
    return True

parser = argparse.ArgumentParser(description="This program \
    counts different loan parameters.")
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--principal", type = int)
parser.add_argument("--payment", type = float)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)
arguments = parser.parse_args()
parameters = [arguments.type, arguments.principal,                                      #list with all arguments
             arguments.payment, arguments.periods, arguments.interest]
type_ = parameters[0]                                                                   #argument "type_" is deciding which kind of loan we calculate

if type_ == "diff":
    if not(parameters[2]) and count_true(parameters) == 4:                              #a condition that checks if the appropriate arguments are specified, in diff "type_" of loan we can calculate only monthly payments
        principal = parameters[1]
        periods = parameters[3]
        interest = parameters[4] / ( 100 * 12)                                          #"interest" is monthly interest in fraction
        sum_ = 0
        if posivite_numbers([principal, periods, interest]):
            for month in range(1, periods + 1):                             
                month_payment = principal / periods + interest * \
                (principal - (principal * (month - 1) / periods))                       #"month_payment" according to the template in the documentation (formula 1.1)
                sum_ += math.ceil(month_payment)                                        #"sum_" is for counting overpayment
                print("Month {}: payment is {}"
                .format(month, math.ceil(month_payment)))
            print("Overpayment = {}".format(sum_ - principal))
    else:
        print("Incorrect parametrs")

elif type_ == "annuity":
    if count_true(parameters) == 4:
        if not(parameters[1]):                                                          #a condition to check that the "principal" parameter is missing
            payment = parameters[2]
            periods = parameters[3]
            interest = parameters[4] / ( 100 * 12)
            if posivite_numbers(parameters[2:5]):
                principal = math.floor(payment /                                        #"principal" according to the template in the documentation (formula 1.2)
                ((interest * math.pow(1 + interest, periods)) /
                (math.pow(1 + interest, periods) - 1)))
                print("Your loan principal = {}!".format(principal))
                print("Overpayment = {:.0f}".format(payment * periods - principal))

        elif not(parameters[2]):                                                        #a condition to check that the "payment" parameter is missing
            principal = parameters[1]
            periods = parameters[3]
            interest = parameters[4] / ( 100 * 12)
            if posivite_numbers([principal, periods, interest]):
                payment = principal * (interest * math.pow(1 + interest, periods)) / \
                (math.pow(1 + interest, periods) - 1)                                   #"payment" according to the template in the documentation (formula 1.3)
                print("Your monthly paymnet = {}!".format(math.ceil(payment)))
                print("Overpayment = {:.0f}"
                      .format(math.ceil(payment) * periods - principal))

        elif not(parameters[3]):                                                        #a condition to check that the "periods" parameter is missing, "periods" = "n"
            principal = parameters[1]
            payment = parameters[2]
            interest = parameters[4] / ( 100 * 12)
            if posivite_numbers([principal, payment, interest]):
                n = math.ceil(math.log(payment /                                        #"n" = "periods" according to the template in the documentation (formula 1.4)
                    (payment - interest * principal), 1 + interest))
                if n / 12 == n // 12:
                    if n // 12 == 1:
                        print("It will take {} year to repay this loan!"
                              .format(n // 12))
                    else:
                        print("It will take {} years to repay this loan!"
                              .format(n // 12))
                elif n == 1:
                    print("It will take 1 month to repay this loan!")
                elif n == 13:
                    print("It will take 1 year and 1 month to repay this loan!")
                elif n < 12:
                    print("It will take {} months to repay this loan".format(n))
                elif n % 12 == 1:
                    print("It will take {} years and 1 month to repay this loan!"
                          .format(n // 12))
                else:
                    print("It will take {} years and {} months to repay this loan!" \
                        .format(n // 12 , n % 12))
            if posivite_numbers([principal, payment, interest]):
                print("Overpayment = {:.0f}".format(payment * n - principal))
    else:
        print("Incorrect parameters.")    