def get_digits(num):
    return [int(i) for i in str(num)]

def calculate(num):
    total = 0
    digits = get_digits(num)
    for i, d in enumerate(digits):
        total += pow(d,i+1)
    return total

def is_disarium(num):
    if calculate(num) == num:
        return True
    return False

num = int(input("Please enter an integer: "))
print(is_disarium(num))