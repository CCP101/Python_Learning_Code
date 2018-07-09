available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings: # 检查是否存在
        print("Adding " + requested_topping + ".")
    elif requested_topping == "green peppers":
        print("Sorry,we are out of green peppers")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

"""
执行一个代码块，使用if-elif-else结构
执行多个代码块，使用一系列独立if语句
"""