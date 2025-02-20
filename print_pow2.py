
def print_pow2(num: int):
    """печатает степень двойки num"""
    n = num
    pow2 = 0
    while num %2==0:
        pow2= pow2+1
        num=int(num/2)
    print (f"{n} = 2^{pow2} * {num}")
for num in [600, 720, 768,800, 900, 960, 1050, 1080, 1440, 1280, 1680,1920, 2160, 2560, 3840]:
    print_pow2(num)
