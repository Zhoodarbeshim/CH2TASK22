t = input()
sign = t[-1]
t = int(t[0:-1])
if sign == 'C':
    t = round(t*(9/5)+32)
    print(str(t) + 'F')
elif sign == 'F':
    t = round((t-32)* (5/9))
    print(str(t) + 'C')