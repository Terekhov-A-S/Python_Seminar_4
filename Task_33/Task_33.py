# Задача 33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0

from random import randint
maximum = 100
k = int(input('Введите натуральную степень k: '))
koeff=[randint(0,maximum) for i in range(k)]+[randint(1,maximum)]
num='+'.join([f'{(j,"")[j==1]} x^{i}' for i, j in enumerate(koeff) if j][::-1])
num=num.replace('x^1 + ', 'x + ')
num=num.replace('x^0', '')
num += ('','1')[num[-1]=='+']
num = (num, num[:-2])[num[-2:]=='^1']
print (f'{num} = 0')