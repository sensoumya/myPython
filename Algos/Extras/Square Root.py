def sub(num, div=0):
    temp = div // 10
    while div * (div % 10) < num and temp == div // 10:
        div += 1
    if div * (div % 10) == num:
        return num - div * (div % 10), div
    div -= 1
    return num - div * (div % 10), div % 10


def sqrt(num):
    num = str(num)
    tag = False
    quot = 0
    if len(num) & 1 == 1:
        rem, div = sub(int(num[:1]))
        quot = div
        num = num[1:]
        tag = True
    while len(num):
        if not tag:
            rem, div = sub(int(num[:2]))
            quot = div
            tag = True
        else:
            rem, div = sub(int(str(rem) + num[:2]), quot * 20)
            quot = quot * 10 + div
        num = num[2:]
    if rem != 0:
        for _ in range(3):
            rem, div = sub(int(str(rem) + '00'), quot * 20)
            quot = quot * 10 + div
        return round(quot / 1000, 2)
    return quot


print(sqrt(200234))
