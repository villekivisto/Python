luku = int(input("Anna luku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("FizzBuzz")

elif luku % 3 == 0:
    print("Fizz")

elif luku % 5 == 0:
    print("Buzz")

else:
    pass