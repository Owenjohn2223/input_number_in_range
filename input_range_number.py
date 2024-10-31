
range_1_10 = 0
range_11_20 = 0


while True:
    try:
        input_number = int(input("Input a number between 1 and 20 (Input a number outside of range to exit): "))

        if 1 <= input_number <= 10:
            range_1_10 += 1
        elif 11 <= input_number <= 20:
            range_11_20 += 1
        else:
            break 

    except ValueError:
        print("Input Invalid")

print("Summary of inputted numbers in the following range:")
print(f"- 1-10 = {range_1_10} ")
print(f"- 11-20 = {range_11_20} ")