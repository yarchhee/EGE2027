# data = "ABCAABACACAB"
# data = data.replace("AB", "A B")
# data = data.split()
# # answer = max(data, key = len)
# # answer = max([len(x) for x in data])
# answer = max(map(len, data))
# print(data, answer)

# 2401
# cпособ 1
# with open("../files/2401.txt") as f:
#     data = f.readline()
#     # делим по сегментам
#     data = data.replace("ad", "a d")
#     data = data.replace("da", "d a")
#     data = data.split()
#     answer = max(data, key=len)
#     print(len(answer))

# способ 2
# with open("../files/2401.txt") as f:
#     data = f.readline()
#
# cur = 1
# max_len = 0
#
# for i in range(len(data)-1):
#     if data[i] + data[i+1] in ("ad","da"):
#         cur = 1
#     else:
#         cur +=1
#     max_len = max(cur, max_len)
# print(max_len)


# 1.
# Текстовый файл состоит не более чем из 106 символов и содержит только
# заглавные буквы латинского алфавита (A..Z). Определите максимальное
# количество идущих подряд символов, среди которых нет сочетания стоящих рядом букв P и R (в любом порядке).
# with open("../files/2401.txt") as f:
#     data = f.readline()
#     # делим по сегментам
#     data = data.replace("PR", "P R")
#     data = data.replace("RP", "R P")
#     data = data.split()
#     answer = max(data, key=len)
#     print(len(answer))
#
# with open("../files/2401.txt") as f:
#     data = f.readline()
#
# cur = 1
# max_len = 0
#
# for i in range(len(data)-1):
#     if data[i] + data[i+1] in ("PR","RP"):
#         cur = 1
#     else:
#         cur +=1
#     max_len = max(cur, max_len)
# print(max_len)
#
# ### 2940
#
# #2
# # Текстовый файл состоит из арабских цифр (0, 1, …, 9).
# # Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет символов 0, стоящих рядом.
# with open("../files/2401.txt") as f:
#     data = f.readline()
#     # делим по сегментам
#     data = data.replace("00", "0 0")
#     # data = data.replace("RP", "R P")
#     data = data.split()
#     answer = max(data, key=len)
#     print(len(answer))
#
# with open("../files/2401.txt") as f:
#     data = f.readline()
#
# cur = 1
# max_len = 0
#
# for i in range(len(data)-1):
#     if data[i] + data[i+1] == "00":
#         cur = 1
#     else:
#         cur +=1
#     max_len = max(cur, max_len)
# print(max_len)

### 977

########type 3

# : Текстовый файл состоит не более, чем из 1 200 000 прописных :
# символов латинского алфавита.
# Определите максимальное количество идущих
# подряд символов, : среди которых любые два символа из набора
# Q, R, S в различных комбинациях (с учётом повторений) не стоят
# рядом.

# with open("2417.txt") as f:
#     data = f.readline()
# # data = "ESCRQPOPQSG"
# data = data.replace("Q", "*")
# data = data.replace("R", "*")
# data = data.replace("S", "*")
#
# while "**" in data:
#     data = data.replace("**", "* *")
#
# data = data.split(" ")
# answer = max(data, key = len)

# Текстовый файл состоит из заглавных букв латинского алфавита
# Q, R, W и цифр 1, 2, 4. Определите в прилагаемом файле максимальное
# количество идущих подряд символов, среди которых ни одна буква не
# стоит рядом с буквой, а цифра - с цифрой.

# with open("16333.txt") as f:
#     data = f.readline()
#
# # for i in "QRW":
# #     data = data.replace(i, "a")
# #
# # for i in "124":
# #     data = data.replace(i, "0")
#
# data = data.replace(str.maketrans("QRW124", "aaa000"))
# while 'aa' in data or "00" in data:
#     data = data.replace("00", "0 0").replace("aa", "a a")
# data = data.split()

# жадный линейный способ

# data = "QRW1Q1112424QQQ1"
# data = data.translate(str.maketrans("QRW124","aaa000"))
#
# max_len = 1
# current_len = 1
#
# for i in range(0, len(data)):
#     if data[i] != data[i-1]:
#         current_len += 1
#         max_len = max(max_len, current_len)
#     else:
#         current_len = 1   2
# print(max_len)




# data = "QRW1Q1112424QQQ1"
# data = data.translate(str.maketrans("QRW124","aaa000"))
#
# left = 0
# max_len = 0
# for right in range(1,len(data)):
#     if data[right] == data[right - 1]:
#         left = right
#     current_len = right - left + 1
#
#     max_len = max(max_len,current_len)
# print(max_len)

# Текстовый файл состоит из символов, обозначающих буквы
# латинского алфавита и десятичные цифры.
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов, среди которых никакие три нечётные
# цифры не стоят рядом.

# with open("13866.txt") as f:
#     data = f.readline()

#
# while "***" in data:
#     data = data.replace("***", "* * *")
# parts = data.split()
# print(data)

# data = "B8HSXLGJ1UAEJ"
#
# for i in "13579":
#     data = data.replace(i, "*")
#
# current_len = 0
# max_len = 0
#
# for i in range(2, len(data)):
#     current_len += 1
#     if data[i] == data[i - 1] == data[i - 2] == "*":
#         current_len = 2
#     max_len = max(max_len, current_len)
# print(max_len)


# Текстовый файл 2411.txt состоит
# из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих
# подряд символов в прилагаемом файле, среди которых
# нет символов 1 и 2, а также 1 и 3 стоящих рядом.

# with open("../files/2411.txt") as f:
#     data = f.readline()
# data = data.replace("12", "**")
# data = data.replace("21", "**")
# data = data.replace("31", "**")
# data = data.replace("13", "**")
# while "**" in data:
#     data = data.replace("**", "* *")
# data = data.split(" ")
# answer = max(data, key = len)
# print(len(answer))

### 339

# жадный

# with open("../files/2411.txt") as f:
#     data = f.readline().strip()
# data = data.translate(str.maketrans("3", "2"))
# max_len = 1
# current_len = 1
# for i in range(1, len(data)):
#     if (data[i] == "1" and data[i-1] == "2") or (data[i] == "2" and data[i-1] == "1"):
#         current_len = 1
#     else:
#         current_len += 1
#         max_len = max(max_len, current_len)
# print(max_len)

### 339

# плавающее
with open("../files/2411.txt") as f:
    data = f.readline().strip()
data = data.translate(str.maketrans("3", "2"))
left = 0
max_len = 1
for right in range(1, len(data)):
    if (data[right] == "1" and data[right - 1] == "2") or (data[right] == "2" and data[right - 1] == "1"):
        left = right
    current_len = right - left + 1
    max_len = max(max_len, current_len)
print(max_len)

