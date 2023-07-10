result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = float(input("Wprowadź liczbę:  "))
            if result == None:
                result = operand
                print(
                    f"Wartość RESULT przy wprowadzaniu liczby: {result}, wartość operandu {operand}"
                )  # only for debuging
                wait_for_number = False
                continue
            else:
                print(
                    f"Wartość2 RESULT przy wprowadzaniu liczby: {result}, wartość2 operandu {operand}"
                )  # only for debugin
                wait_for_number = False
                continue
        except ValueError:
            print("Błędna wartość! ")
            continue
    else:
        operator = input("'+', '-', '*', '/' lub '=' to finish ")
        print(
            f"Wartość result po wprowadzeniu operatora {result}, wartość operandu {operand}"
        )  # only for debuging
        """if result == None:
            result = operand
            wait_for_number = True
            continue
        else:"""
        if operator == "+":
            result += operand
            wait_for_number = True
            continue
        elif operator == "-":
            result -= operand
            wait_for_number = True
            continue
        elif operator == "*":
            result *= operand
            wait_for_number = True
            continue
        elif operator == "/":
            result /= operand
            wait_for_number = True
            continue
        elif operator == "=":
            print(result)
        else:
            print("błędna wartość operatora!")
            continue
        break
