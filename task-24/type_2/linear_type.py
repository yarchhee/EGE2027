##### задание 2416

data = "AABECAEABECADA"
chars = "AE"
i = 0
max_len = 0
cnt = 0
while i < len(data):
    if data[i] in chars and data[i+1] not in chars:
        i +=2
        cnt += 1
        max_len = max(cnt, max_len)
    else:
        i += 1
        cnt = 0
print(max_len)