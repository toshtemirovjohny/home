def count_vowels_and_consonants(matn: str):
    x = {}
    count_unli = 0 ; count_undosh = 0
    for harf in matn.lower():
        if harf.isalpha():
            if harf in 'aioue':
                count_unli += 1
            else:
                count_undosh += 1

    x['unli'] = count_unli 
    x['undosh'] = count_undosh
    return x

matn = input("Matn kiriting -> ")
print(count_vowels_and_consonants(matn))
