numbers = [2, 7, 11, 15, 3, 4, 6]
desired_sum = int(input('Введите желаемую сумму '))
for resutl in range(len(numbers)-1):
    if (numbers[resutl]+(numbers[resutl+1])) == desired_sum:
        print([resutl,resutl+1])