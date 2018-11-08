for i in range(0, 200):
    print(i)

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 900, 50]
for i in range(len(names)):
    print(names[i])
for names, ages in zip(names, ages):
    print(names, "is", ages)

print(sorted("hello,world"))

print([x * x for x in range(20)])

# pass 占位符

# del 删除

exec("print('hello,world')")
print(eval(input("Please input ")))
