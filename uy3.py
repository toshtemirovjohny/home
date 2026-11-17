# 🎯 Maqsad
# Sonlar ro'yxatini chastotasiga qarab kamayish tartibida saralash. 
# 'Chastotasi teng bo'lgan sonlar — qiymati bo'yicha o'sish tartibida joylashsin.

def rearrange_by_frequency(nums: list[int]):
    a = {}
    for i in nums:
        count = 0
        for x in nums:
            if x == i:
                count +=1
        a[i] = count
    natija = sorted(a.keys(), key=lambda x: (-a[x],x))
    return natija

sonlar = [4, 5, 6, 5, 4, 3, 4]

print(rearrange_by_frequency(sonlar))