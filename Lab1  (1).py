text = input()
key = 1
alf = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
symbol ="  {{}}[[]](())--==++//**"
result = ""
for i in range(len(text)):
    if str(text[i]) in alf:
        t = alf.find(str(text[i]))
        result += alf[t + key]
    elif str(text[i]) in symbol:
        result += symbol[symbol.find(str(text[i]))]
print(result)