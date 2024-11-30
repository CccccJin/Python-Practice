a = []
Max = 0
Min = 0

while True:
    num = input("Please enter a number:")
    if num == 'Done':
        break
    try:
        num = float(num)  # 尝试将输入转换为浮点数
    except ValueError:
        print('PLZ ENTER NUMBER!!')
        continue
    a.append(num)
    Max = max(a)
    Min = min(a)
    
print('Maximum:',float(Max))
print('Minimum:',float(Min))
print(a)
