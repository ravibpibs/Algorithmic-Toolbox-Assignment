nums = []
while True:
        num = input("Enter a number: ")
        if num == 'done':
            break
        try:
            nums.append(int(num))
        except ValueError:
            print("Invalid input")
            break
print("Maximum is {}".format(max(nums)))
print("Minimum is {}".format(min(nums)))




