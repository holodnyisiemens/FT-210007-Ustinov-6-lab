from statistics import geometric_mean

print ('Данная программа рассчитывает весовые коэффициенты критериев оценивания\n'
       'по методу анализа иерархий (МАИ) Томаса Саати')

while True:     # цикл обработки ввода количества критериев
    try:
        criteria_number = int(input('Введите целое число - кол-во критериев: '))
        break
    except:
        print ('Ошибка ввода')

data_matrix = []  # матрица для данных сравнения критериев

for i in range(criteria_number):   # циклы для ввода данных сравнения критериев
    matrix_row = []  # строка матрицы
    
    for j in range(criteria_number):
        if i == j: # сравнение одинаковых критериев
            comparison = 1
        elif i > j: # повторная (лишняя) попытка сравнения
            comparison = 1 / data_matrix[j][i]  # ввод обратного числа в матрицу
        else:
            while True:     # цикл обработки ввода данных сравнения критерия
                try:
                    comparison = float(input(f'Введите сравнение критерия {i + 1} и {j + 1}: '))
                    break
                except:
                    print ('Ошибка ввода')
        matrix_row.append(comparison)   # добавление очередного критерия
        
    data_matrix.append(matrix_row)  # добавление очередной строки в матрицу

summ = 0   # сумма средних геометрических
list_of_averages = []   # список средних геометрических

for c in range(criteria_number): # цикл заполнения списка средних геометрических
    average = geometric_mean(data_matrix[c])    # вычисление среднего геометрического
    summ += average
    list_of_averages.append(average)

for l in range(criteria_number):    # цикл вывода весового коэффициента критериев
    weight_factor = list_of_averages[l] / summ
    print (f'Весовой коэффициент {l + 1} критерия: {round(weight_factor, 2)}')
