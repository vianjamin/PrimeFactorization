
def prime_factor(n):
# prime_candidate = int(input("Enter your number \n"))
    number = 2
    factor = []
    while n > 1:
        result = n % number
        if result == 0:
            n /= number
            factor.append(number)
        elif result != 0:
            number += 1
    return factor


while True:

    num = int(input("Please input your number\n"))
    factors = prime_factor(num)
    print(factors)
    choice = input("Do you want to go again? Y or N").lower().strip()
    if choice == "n":
        print("Cheers")
        break
