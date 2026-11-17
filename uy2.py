products = {"Olma": 5000, "Banan": 8000, "Uzum": 7000}
sales = {"Olma": 10,   "Banan": 5,    "Uzum": 8}

def find_top_seller(products: dict, sales: dict):
    x = {}
    for p,s in zip(products,sales):
        # print(p,sales[s])
        x[p] = products[x]*sales[s]
    print(x)


find_top_seller(products,sales)