# Выходные данные
# Программа должна вывести nn-ый член геометрической прогрессии.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1
# 2
# 5
# Sample Output 1:
#
# 16
# Sample Input 2:
#
# 10
# -2
# 6
# Sample Output 2:
#
# -320
# Sample Input 3:
#
# -2
# 10
# 3
# Sample Output 3:
#
# -200

b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n-1))