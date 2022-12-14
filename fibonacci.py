def fibo(num, inital_val, second_val, series):
    if num == 1:
        return series
    else:
        third_val = inital_val + second_val
        inital_val = second_val
        second_val = third_val
        series.append(third_val)
        return fibo(num - 1, inital_val, second_val, series)


series = []
first_val = 0
second_val = 1
series.append(first_val)
series.append(second_val)
pos = input("Enter the position for the series = ")
res = fibo(int(pos) - 1, first_val, second_val, series)
print("The fibonacci series upto " + pos + "th position are ")
print(res)
