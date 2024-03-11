def find_numbers():
    count = 0
    number = 600000

    while count < 5:
        number += 1
        divisor_found = False
        derg = None

        for divisor in range(2, number):
            if number % divisor == 0:
                if str(divisor)[-1] == '7' and divisor != 7 and divisor != number:
                    divisor_found = True
                    derg = divisor
                    break

        if divisor_found:
            print(number, derg)
            count += 1
            
find_numbers()

