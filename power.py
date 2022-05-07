b = int(input("enter base"))
exp = int(input("enter exponent"))
result = 1
while exp != 0:
    result *= b
    exp-=1
print(result)