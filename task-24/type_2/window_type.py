##### задание 2416

data = "AABECAEABEECADA"
chars = "AE"
left = right = 0
max_len = 0
while right < len(data)-1:
    if data[right] in chars and data[right+1] not in chars:
        right += 2
        current_len = (right - left) // 2
        max_len = max(max_len, current_len)
    else:
        right += 1
        left = right
print(max_len)
