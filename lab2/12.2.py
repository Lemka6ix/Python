def expression():
    result = 3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2 * 4**4 + 1
    return result

result_value = expression()
death = hex(result_value)[2:]
print(death)

def count_zeros(number):
    number_str = str(number)
    count = number_str.count('0')
    return count

zeros_count = count_zeros(death)
print("Кол-во значимых нулей - ", zeros_count)