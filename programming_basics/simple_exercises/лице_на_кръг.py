import math

r = float(input())
pi = math.pi

s = pi * r * r
p = 2 * pi * r

s_format = format(s, '0.2f')
p_format = format(p, '0.2f')

print(s_format)
print(p_format)
