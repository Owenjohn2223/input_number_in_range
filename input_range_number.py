
range_numbers = [0] * 5

while True:
    try:
        input_number = int(input("Input a number between 1 and 50 (or a number outside of range to exit): "))

        if 1 <= input_number <= 10:
            range_numbers[0] += 1
        elif 11 <= input_number <= 20:
            range_numbers[1] += 1
        elif 21 <= input_number <= 30:
            range_numbers[2] += 1
        elif 31 <= input_number <= 40:
            range_numbers[3] += 1
        elif 41 <= input_number <= 50:
            range_numbers[4] += 1
        else:
            print("///Exiting Program...///")
            break 

    except ValueError:
        print("///Input Invalid///")

print("--- Summary of inputted numbers in the following range ---")
print(f"\t1 - 10 = {range_numbers[0]} ")
print(f"\t11 - 20 = {range_numbers[1]} ")
print(f"\t21 - 30 = {range_numbers[2]} ")
print(f"\t31 - 40 = {range_numbers[3]} ")
print(f"\t41 - 50 = {range_numbers[4]} ")

