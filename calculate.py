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
            if operator:
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    result /= operand
            wait_for_number = False
            continue
        except ValueError:
            print("Błędna wartość! ")
            continue
    else:
        operator = input("'+', '-', '*', '/' lub '=' to finish ")
        if operator == "=":
            print(result)
        elif operator in ("+", "-", "*", "/"):
            wait_for_number = True
            continue
        else:
            print("błędna wartość operatora!")
            continue
    break
    '''
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
    '''
