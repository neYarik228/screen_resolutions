
def print_pow2(num: int):
    """печатает степень двойки num"""
    n = num
    pow2 = 0
    while num %2==0:
        pow2= pow2+1
        num=int(num/2)
    print (f"{n} = 2^{pow2} * {num}")

num = input("введите число")
num = int(num)
print_pow2(num)
    