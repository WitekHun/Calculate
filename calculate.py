result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:
        try:
            operand = float(input("Wprowadź liczbę "))
            wait_for_number = False
            if result == None:
                result = operand
                print(f"RESULT {result}")
            continue
        except ValueError:
            print("Błędna wartość! ")
            continue
    else:
        operator = input("'+', '-', '*', '/' lub '=' to finish ")

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
