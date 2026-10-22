num = int(input("Enter a number: "))
while num <= 0:
    print("Please enter a whole number greater than zero")
    num = int(input("Enter a number: "))
S = num * (num + 1) / 2
print(f"Expected sum is: {S:.2f}")

def get_sum (a):
    sum = 0
    for i in range(1, a + 1):
        sum += i
    return sum

actual_sum = get_sum(num)
print(f"After calling the function get_sum, the sum of all numbers from 1 to {num} is: {actual_sum:.2f}")

if S == actual_sum:
    print("Output Verified.)")