from math_function import add

def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":  # Check for multiplication
        result = multiply(data_1, data_2)
    elif operator == "/":  # Check for division
        try:
            result = divide(data_1, data_2)
        except ValueError as e:
            print("Error:", e)
            return  # Exit the program in case of division by zero
    else:
        print("Operator not supported")
        return  # Exit the program for unsupported operators

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if _name_ == "_main_":
    print("Hello Main !")
    main()