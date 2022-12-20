def main():

    while True:
        try:
            cc_number = int(input("Credit Card Number: "))
            if cc_number > 0:
                break
        except ValueError: #instead of crashing, do this and continue (in this case prompt again)
            print("Invalid Input: Try Again")

    num1 = (cc_number % 100) // 10
    num2 = (cc_number % 10000) // 1000
    num3 = (cc_number % 1000000) // 100000
    num4 = (cc_number % 100000000) // 10000000
    num5 = (cc_number % 10000000000) // 1000000000
    num6 = (cc_number % 1000000000000) // 100000000000
    num7 = (cc_number % 100000000000000) // 10000000000000
    num8 = (cc_number % 10000000000000000) // 1000000000000000

    num1 = num1*2
    num2 = num2*2
    num3 = num3*2
    num4 = num4*2
    num5 = num5*2
    num6 = num6*2
    num7 = num7*2
    num8 = num8*2

    new_num1 = (num1 % 10) + ((num1 % 100) // 10)
    new_num2 = (num2 % 10) + ((num2 % 100) // 10)
    new_num3 = (num3 % 10) + ((num3 % 100) // 10)
    new_num4 = (num4 % 10) + ((num4 % 100) // 10)
    new_num5 = (num5 % 10) + ((num5 % 100) // 10)
    new_num6 = (num6 % 10) + ((num6 % 100) // 10)
    new_num7 = (num7 % 10) + ((num7 % 100) // 10)
    new_num8 = (num8 % 10) + ((num8 % 100) // 10)

    num9 = (cc_number % 10)
    num10 = (cc_number % 1000) // 100
    num11 = (cc_number % 100000) // 10000
    num12 = (cc_number % 10000000) // 1000000
    num13 = (cc_number % 1000000000) // 100000000
    num14 = (cc_number % 100000000000) // 10000000000
    num15 = (cc_number % 10000000000000) // 1000000000000
    num16 = (cc_number % 1000000000000000) // 100000000000000

    sumA = new_num1 + new_num2 + new_num3 + new_num4 + new_num5 + new_num6 + new_num7 + new_num8
    sumB = num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16
    sumC = sumA + sumB

    if (sumC % 10) > 0:
        print("INVALID")
        exit()

    length = len(str(cc_number))
    first_two = int(cc_number / (10 ** (length - 2)))

    if (length == 15) and ((first_two == 34) or (first_two == 37)):
        print("AMEX")

    elif ((length == 16) or (length == 13)) and (first_two // 10 == 4):
        print("VISA")

    elif (length == 16) and ((first_two == 51) or (first_two == 52) or (first_two == 53) or (first_two == 54) or (first_two == 55)):
        print("MASTERCARD")

    else:
        print("INVALID")

main()