####### задание 2416
data = "AABECAEABECADA"
pairs = ["AB","AC","AD","EB","EC","ED"]
for i in pairs:
    data = data.replace(i, "*")
for i in "ABCDE":
    data = data.replace(i, " ")
data = data.split()
max_data = max(data, key=len)
print(len(max_data))