# 🎯 Maqsad
# Mahsulot narxlari va sotuv soni berilganda, 
# eng ko'p tushum keltirgan mahsulot nomini topuvchi funksiya yozish.

products = {"Olma": 5000, "Banan": 8000, "Uzum": 7000}
sales = {"Olma": 10,   "Banan": 5,    "Uzum": 8}

def find_top_seller(products: dict, sales: dict):
    x = {}
    for p,s in zip(products,sales):
        # print(p,sales[s])
        x[p] = products[p]*sales[s]
    eng_max = max(x, key=lambda a: x[a])
    return f"Eng ko'p tushum: {eng_max} {x[eng_max]} so'm"


print(find_top_seller(products,sales))

