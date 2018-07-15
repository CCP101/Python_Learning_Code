filename = 'pi_digits.txt'

with open(filename) as file_object:  # 省去文件流，自动关闭
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())  # 删除EOF 文件结尾  并且删除多余换行符号

# windows系统中为防止地址被转义前面加一个r
