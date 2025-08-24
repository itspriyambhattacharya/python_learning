from decimal import Decimal
n = 1
print(n << 2)

m = 8

print(m >> 2)

x = 0.1
y = 0.3
res = x+x+x-y  # problem
print(res)

y = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
print(y)
print(type(y))
