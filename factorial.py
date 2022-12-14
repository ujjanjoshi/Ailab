def fact(num, inti_value):
    if (num == 1):
        return inti_value
    else:
        inti_value = inti_value * num
        return fact(num - 1, inti_value)


intial_value = 1
input_value = input("Enter the number you want to get factorial:\n")
final_value = fact(int(input_value), intial_value)
print("The factorial of " + input_value + "! = " + str(final_value))
