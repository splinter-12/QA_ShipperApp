result_a = "Chrome"
result_b = "FireFox"
result_c = "internet explorer"
result_d = "edge"
print("1."+result_a+" \n2."+result_b+" \n3."+result_c+" \n4."+result_d+" \nEnter:")
option = int(input(" "))


def switch(choice):
    if choice == 1:
        import chrome
        print("Using "+result_a)

    elif option == 2:
        import firefox
        print("Using "+result_b)

    elif option == 3:
        import ie
        print("Using "+result_c)  

    elif option == 4:
        import edge
        print("Using "+result_d)     
     
    else:
        print("Incorrect option")

switch(option)

