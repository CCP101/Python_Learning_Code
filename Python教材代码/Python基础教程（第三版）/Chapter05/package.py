x, y, z = 1, 2, 3
print(x, y, z)

scounrel = {"name": "Robin", "girlfriend": "Marion"}
key, value = scounrel.popitem()
print(key, value)

a, b, *sert = 1, 2, 3, 4
print(sert)

# 三目运算符python版本
status = "friend" if x == 1 else "fooler"

if a < 0:
    print("a<0")
elif a == 0:
    print("a=0")
else:
    print("a>0")

# x is y
# x is not y
# is 检查是否相同而不是相等
# x in y
# x not in y

print("a".lower() < "B".lower())
assert 0 < x < 100