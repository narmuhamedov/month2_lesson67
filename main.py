numbers = [2, 7, 11, 15, 3, 4, 6]
desired_sum = int(input('Введите желаемую сумму '))
for i in range(len(numbers)-1):
    if (numbers[i]+(numbers[i+1])) == desired_sum:
        print([i, i+1])