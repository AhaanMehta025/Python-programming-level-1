print("This is the FizzBuzz project! it checks whether your number is divisible by 5, 3, or both.")

a = int(input("Enter a number: "))

if(a%5 ==0 and a%3 ==0):
    print("FizzBuzz")

elif a%3 == 0:
    print("Fizz")

elif a%5 == 0:
    print("Buzz")

else:
    print (a)

