# defines first and second inputs from user
def user_input(first, second):
    # checks validation for first input
    if type(first) == int:
        if first > 100:
            print("pass")
        elif first == 100:
            print("ok")
        else:
            print("fail")
    else:
        print("invalid")
    # checks validation for second input
    if type(second) == str:
        print("valid")
    else:
        pass
# sample first and second inputs        
user_input(28, "foobar")  