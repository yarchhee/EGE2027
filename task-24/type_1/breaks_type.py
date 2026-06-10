# Текстовый файл 16333 состоит из
# заглавных букв латинского алфавита Q, R, W и цифр 1, 2, 4.
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов, среди которых ни одна буква не
# стоит рядом с буквой, а цифра - с цифрой.
import string

with open("../files/16333.txt") as f:
    data = f.readline()
data = data.translate(str.maketrans("QRW124", "aaa000"))

breaks = []

for mistake in range(1, len(data)):
    if data[mistake] == data[mistake - 1]:
        breaks.append(mistake)

breaks.append(len(data)-1)

max_len = 0
for i in range(1, len(breaks)):
    distance = breaks[i] - breaks[i - 1]
    max_len = max(max_len, distance)
print(max_len)

