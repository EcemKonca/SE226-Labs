calculation = lambda n: (n - 3) / n ** 2
number = int(input("Enter the number: "))
List = []
for i in range(1, number + 1, 1):
    List.append(calculation(i))
print("Your result is:", sum(List))


def calculation2(n):
    """This function calculates product recursively """
    if n == 0:
        return 1
    else:
        return (n / (n + 2) - 10) * calculation2(n - 1)


number2 = int(input("Enter the number: "))
print(calculation2.__doc__)
print(calculation2(number2))
