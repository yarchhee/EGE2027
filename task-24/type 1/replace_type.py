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

