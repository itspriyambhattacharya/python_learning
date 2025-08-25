from decimal import Decimal
import fractions
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


f1 = fractions.Fraction(2, 5)
f2 = fractions.Fraction(3, 6)
print(f1+f2)
print(f1.numerator)

s1 = {1, 2, 3, 4}
s2 = {1, 3, 7}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.difference(s1))
