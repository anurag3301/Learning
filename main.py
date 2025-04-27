def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if isEven(num):
    print("Number you entered is even")
else:
    print("Number you entered is odd")
