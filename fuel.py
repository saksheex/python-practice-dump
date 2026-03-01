import fractions


while True:
    try:
        user = fractions.Fraction(input("Fraction: "))
        if user.numerator > user.denominator:
            continue
        if user.numerator < 0:
            continue
        result = round(user * 100)
        if result >= 99:
            print("F")
        elif result <= 1:
            print("E")
        else:
            print(f"{result}%")
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue 