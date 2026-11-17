# 🎯  Maqsad
# JSON fayldan talabalar ma'lumotlarini o'qib, 
# eng yaxshi va eng past baholi talabani hamda 
# o'rtacha bahoni topib ekranga chiqaruvchi dastur yozish.

import json

with open("students.json") as fayl:
    data = json.load(fayl)

# print(data)

x = {}
for i in data:
    ism = i['name']
    baho = i['grade']
    x[ism] = baho

baho_sum = sum(x.values())
eng_max = max(x, key=lambda a: x[a])
eng_min = min(x, key=lambda a: x[a])
avg_baho = round(baho_sum/len(data), 1)

print(f"Eng yuqori baho: {eng_max} {x[eng_max]} ball")
print(f"Eng past baho: {eng_min} {x[eng_min]} ball")
print(f"O'rtacha baho: {avg_baho} ball")