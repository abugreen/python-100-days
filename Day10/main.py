from art import logo

print(logo)

def cal_number(first_number,next_number,operation):
    if operation == "+":
        return (float(first_number) + float(next_number))
    elif operation == "-":
        return (float(first_number) - float(next_number))
    elif operation == "*":
        return (float(first_number) * float(next_number))
    elif operation == "/":
        return (float(first_number) / float(next_number))

def show_opeation():
    print("+")
    print("-")
    print("*")
    print("/")

run_flag = True
cont_or_exit = " "
while run_flag:
    if cont_or_exit == "y":
        first_number = result
    else:
        first_number =input("What's the first number?:")
    show_opeation()
    opeation = input("Pick an operation:")
    next_number = input("What's the next number?:")
    result = cal_number(first_number , next_number , opeation)
    print(f"{first_number} {opeation} {next_number} = {result}")

    cont_or_exit = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    # if cont_or_exit == "n":
    #     run_flag = False
    #     print("Bye Bye")
        

